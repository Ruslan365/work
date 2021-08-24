from django.http import HttpResponse
from django.shortcuts import render
from users.models import User
from posts.models import Post
from .models import Group


def members_view(request):
    userss = Group.objects.all()
    users = userss.first()
    query = User.objects.birthdays()
    recent_posts = Post.objects.filter(is_published=1)[:5:]
    return render(
        request,
        "../templates/intranet/home/members.html",
        {
            'users': users,
            "birthdays":query,
            "recent_posts":recent_posts,
        },
        )