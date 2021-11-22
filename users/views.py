from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from .forms import UserForm
from .models import User
from django.shortcuts import render, get_object_or_404, redirect
from posts.models import Post, Tag
from posts.forms import PostForm

@login_required(login_url="localhost/login/")
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


@login_required(login_url="localhost/login/")
def profile_page(request, id):
    queryset = User.objects.birthdays()
    new_post = None
    tags = Tag.objects.all()
    user = get_object_or_404(User, id=id)
    user_posts = Post.objects.filter(author__id=id)
    recent_posts = Post.objects.filter(is_published=1)[:5:]
    if request.method == "POST":
        post_form = PostForm(request.POST, request.FILES)
        if post_form.is_valid():
            preview_pic = post_form.cleaned_data.get("preview_pic")
            title = request.POST.get("title")
            body = request.POST.get("body")
            tag = post_form.cleaned_data.get("tag")
            new_post = Post.objects.create(
                preview_pic= preview_pic,
                author=request.user,
                title=title,
                body=body,
                is_published=1,
                slug=title,
            )
            new_post.save()
            tag = request.POST.get("tag")
            if tag:
                splitted_tags = tag.split(", ")
                tags = Tag.objects.none()
                for tag in splitted_tags:
                    if not Tag.objects.filter(name = tag):
                        Tag.objects.create(name = tag)
                    tags = tags | Tag.objects.filter(name = tag)
                for t in tags:
                    new_post.tag.add(t)
            new_post.save()
            return redirect(f"localhost/profile/dge{request.user.id}du/")
    else:
        post_form = PostForm()
    return render(
        request,
        "intranet/user/profile.html",
        {
            "user": user,
            "tags":tags,
            # "social_networks": social_networks,
            "user_posts": user_posts,
            "post_form": post_form,
            "recent_posts": recent_posts,
            "birthdays": queryset,
        },
    )

@login_required(login_url="localhost/login/")
def profile_editor(request, id):
    recent_posts = Post.objects.filter(is_published=1)[:5:]
    queryset = User.objects.birthdays()
    user = User.objects.get(id=id)
    form = UserForm(instance=user)
    if request.method == "POST":
        # form = UserForm(request.POST, instance=request.user)
        form = UserForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            user.avatar = form.cleaned_data.get("avatar")
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.about = request.POST.get("about")
            user.facebook_id = request.POST.get("facebook_id")
            user.twitter_id = request.POST.get("twitter_id")
            user.birth_date = request.POST.get("birth_date")
            user.save()
            return redirect(f"http://127.0.0.1:8000/profile/dge{id}du/")
        else:
            form = UserForm()
    return render(
        request,
        "intranet/user/profile_editor.html",
        {"form": form, "avatar": user.avatar,
         "recent_posts":recent_posts,
         "birthdays": queryset,
         },
    )


def organization_page(request):
    roles = Role.objects.all()
    return render(
        request,
        "intranet/organization.html",
        {"roles": roles},
    )
