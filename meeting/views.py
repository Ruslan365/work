from django.shortcuts import render
from users.models import User


def meet_page(request):
    emails = user_emails = User.objects.values_list("email", flat=True)
    return render(
        request,
        "../templates/intranet/home/dir.html",
        {
            "user_emails": emails,
        },
    )
