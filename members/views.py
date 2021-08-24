from django.http import HttpResponse
from django.shortcuts import render
from users.models import User
from .models import Group

def members_view(request):
    userss = Group.objects.all()
    users = userss.first()
    return render(
        request,
        "../templates/intranet/home/members.html",
        {
            'users': users
        },
        )