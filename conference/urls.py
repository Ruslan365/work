from django.urls import path
from conference.views import search_call

urlpatterns = [
    path("conference/", search_call, ),
]
