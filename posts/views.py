from django.shortcuts import render, get_object_or_404, redirect

from posts.models import Post, Comment, LikeDislike
from posts.forms import CommentForm, PostForm, SearchForm
from users.models import User
from django.contrib.auth.decorators import login_required
from elasticsearch_dsl.query import MultiMatch
from elasticsearch_dsl import Search
from elasticsearch import Elasticsearch
import json
from django.http import HttpResponse
from django.views import View
from django.contrib.contenttypes.models import ContentType
from polls.forms import PollAddForm

@login_required(login_url="http://127.0.0.1:8000/accounts/login/")
def post_list(request):
    recent_posts = Post.objects.filter(is_published=1)[:5:]
    return render(
        request,
        "intranet/home/post/list.html",
        {
            "recent_posts": recent_posts,
        },
    )


@login_required(login_url="http://127.0.0.1:8000/accounts/login/")
def post_detail(request, pk):
    post =  Post.objects.get(pk=pk)
    # post.views_counter += 1
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
        "../templates/intranet/home/post/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "form": comment_form,
            "tags": tags,
            "recent_posts": recent_posts,
        },
    )


@login_required(login_url="http://127.0.0.1:8000/accounts/login/")
def comment_page(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    return render(request, 'intranet/home/post/comment_page.html', {'comment':comment})


@login_required(login_url="http://127.0.0.1:8000/accounts/login/")
def tag_page(request, tag):
    posts = Post.objects.filter(tag__name=tag)
    return render(
        request,
        "intranet/home/tag_page.html",
        {
            "posts": posts,
        },
    )


@login_required(login_url="http://127.0.0.1:8000/accounts/login/")
def home_page(request):
    user = User.objects.get(email=request.email)
    recent_posts = Post.objects.get(is_published=1)[:5:]
    online_users = User.objects.is_online.all[:5:]
    return render(request, "intranet/home/home_page.html", {"user": user, "recent_posts":recent_posts, "users_online":online_users,})


@login_required(login_url="http://127.0.0.1:8000/accounts/login/")
def post_creator(request, id):
    user = request.user
    new_post = None
    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            preview_img = post_form.cleaned_data.get("preview_pic")
            title = request.POST.get("title")
            body = request.POST.get("body")
            tag = request.POST.get("tag")
            new_post = Post.objects.create(
                author=request.user,
                title=title,
                body=body,
                is_published=1,
                slug=title,
            )
            new_post.save()
            if tag:
                for t in tag.iterator():
                    new_post.tag.add(t)
            return redirect(f"http://127.0.0.1:8000/profile/dge{request.user.id}du")
    else:
        post_form = PostForm()

    return render(
        request,
        "intranet/user/post_creator.html",
        {
            "user": user,
            "post_form": post_form,
            # "email": email,
        },
    )




@login_required(login_url="http://127.0.0.1:8000/accounts/login/")
def profile_page(request, id):
    user = get_object_or_404(User, id=id)
    user_posts = Post.objects.filter(author__id=id)
    # social_networks = dict(user.social_network.values("social_network_name", "social_network_link"))
    return render(
        request,
        "intranet/user/profile.html",
        {
            "user": user,
            # "social_networks": social_networks,
            "posts": user_posts,
        },
    )


def post_search(request):
    form = SearchForm()
    client = Elasticsearch()
    if "query" in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            search_query = form.cleaned_data["query"]
            q = MultiMatch(query=search_query, fields=["title", "body", "description"], fuzziness="AUTO")
            s = Search(using=client, index="posts").query(q)
            response = s.execute()
            ids=[]
            all_posts=[]
            for hit in response:
                all_posts.append(Post.objects.get(id=hit.id))
            return render(
                request,
                "intranet/home/search_page.html",
                {
                    "form": form,
                    "query": search_query,
                    "results": all_posts,
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