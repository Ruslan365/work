from django.shortcuts import render
from users.models import User


def get_email_list(request):
    all_user_emails = list(User.objects.all().values_list("email", flat=True))
    return all_user_emails


def dir(request):
    return render(request, "../templates/intranet/home/dir.html")
