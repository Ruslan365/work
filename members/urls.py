from django.urls import path
from members.views import members_view

urlpatterns = [
    path("members/", members_view,),
]
