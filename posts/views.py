from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post, Comment, LikeDislike
from posts.forms import CommentForm, PostForm, SearchForm
from users.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from elasticsearch import Elasticsearch
import json
from django.http import HttpResponse
from django.views import View
from django.contrib.contenttypes.models import ContentType


@login_required(login_url="/login/")
def post_list(request):
    queryset = User.objects.birthdays()
    recent_posts = Post.objects.filter(is_published=1)[:5:]
    return render(
        request,
        "intranet/post/post_list.html",
        {
            "recent_posts": recent_posts,
            "birthdays": queryset,
        },
    )


@login_required(login_url="/login/")
def post_detail(request, pk):
    queryset = User.objects.birthdays()
    post = Post.objects.get(pk=pk)
    post.post_views += 1
    post.save()
    comments = Comment.objects.filter(post=post, active=True, reply=None)
    recent_posts = Post.objects.filter(is_published=1)[:5:]
    tags = post.tag.all()
    if request.method == "POST":
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            body = request.POST.get("body")
            reply_id = request.POST.get("comment_id")
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post, author=request.user, body=body, reply=comment_qs)

            comment.save()
            return redirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
    return render(
        request,
        "../templates/intranet/post/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "form": comment_form,
            "tags": tags,
            "recent_posts": recent_posts,
            "birthdays": queryset,
        },
    )


@login_required(login_url="/login/")
def comment_page(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return render(request, 'intranet/post/comment_page.html', {'comment': comment})


@login_required(login_url="/login/")
def tag_page(request, tag):
    posts = Post.objects.filter(tag__name=tag)
    return render(
        request,
        "intranet/tag_page.html",
        {
            "posts": posts,
        },
    )


@login_required(login_url="/login/")
def home_page(request):
    titles = []
    queryset = User.objects.birthdays()
    user = User.objects.get(id=request.user.id)
    recent_posts = Post.objects.filter(is_published=1)[:5:]
    btninfo = Post.objects.all()
    return render(request, "intranet/home/home_page.html",
                  {"user": user, "recent_posts": recent_posts, "birthdays": queryset, "btninfo": btninfo})


def post_search(request):
    queryset = User.objects.birthdays()
    recent_posts = Post.objects.filter(is_published=1)[:5:]

    form = SearchForm()
    client = Elasticsearch()
    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data["query"]
            q_splitted = search_query.split(" ")
            all_users = User.objects.filter(
                Q(first_name__icontains=f"{q_splitted[0]}") | Q(last_name__icontains=f"{q_splitted[0]}"))
            all_posts = Post.objects.filter(
                Q(title__icontains=f"{q_splitted[0]}") | Q(body__icontains=f"{q_splitted[0]}") | Q(
                    description__icontains=f"{q_splitted[0]}"))
            for search_word in q_splitted:
                all_users = all_users & User.objects.filter(
                    Q(first_name__icontains=f"{search_word}") | Q(last_name__icontains=f"{search_word}"))
                all_posts = all_posts & Post.objects.filter(
                    Q(title__icontains=f"{search_word}") | Q(body__icontains=f"{search_word}") | Q(
                        description__icontains=f"{search_word}"))
            posts_counted = all_posts.count()
            users_counted = all_users.count()
            return render(
                request,
                "intranet/post/search_page.html",
                {
                    "form": form,
                    "query": search_query,
                    "posts_counted":posts_counted,
                    "users_counted": users_counted,
                    "results_posts": all_posts[0:5:-1],
                    "results_users": all_users[:5],
                    "birthdays": queryset,
                    "recent_posts": recent_posts,
                },
            )


class VotesView(View):
    model = None  # Модель данных - Статьи или Комментарии
    vote_type = None  # Тип комментария Like/Dislike

    # @method_decorator(csrf_exempt)
    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        # GenericForeignKey не поддерживает метод get_or_create
        try:
            likedislike = LikeDislike.objects.get(content_type=ContentType.objects.get_for_model(obj), object_id=obj.id,
                                                  user=request.user)
            if likedislike.vote is not self.vote_type:
                likedislike.vote = self.vote_type
                likedislike.save(update_fields=['vote'])
                result = True
            else:
                likedislike.delete()
                result = False
        except LikeDislike.DoesNotExist:
            obj.votes.create(user=request.user, vote=self.vote_type)
            result = True

        return HttpResponse(
            json.dumps({
                "result": result,
                "like_count": obj.votes.likes().count(),
                "dislike_count": obj.votes.dislikes().count(),
                "sum_rating": obj.votes.sum_rating()
            }),
            content_type="application/json"
        )
