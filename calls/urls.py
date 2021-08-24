from django.urls import path

from calls.views import search_call

urlpatterns = [
    path("dir/", search_call, ),
]
