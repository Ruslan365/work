from django.shortcuts import render


def dir(request):
    return render(request, "../templates/intranet/home/dir.html")
