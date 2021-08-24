from django.shortcuts import render
from .models import Work
from users.models import User
from posts.models import Post

def vacancies_view(request):
    queryset = User.objects.birthdays()
    recent_posts = Post.objects.filter(is_published=1)[:5:]
    www = Work.objects.all()
    return render(
        request, "../templates/intranet/home/vacancies.html",
        {"www": www,
         "birthdays":queryset,
         "recent_posts":recent_posts})