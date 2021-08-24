from django.shortcuts import render
from .models import Work

def vacancies_view(request):
    www = Work.objects.all()
    return render(
        request, "../templates/intranet/home/vacancies.html", {"www": www})
