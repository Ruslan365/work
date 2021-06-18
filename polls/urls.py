from django.urls import path
from . import views

app_name = "polls"

urlpatterns = [
    path('list/', views.polls_list, name='list'),
    path('poll/<int:poll_id>/edit/', views.polls_edit, name='edit'),
    path('poll/<int:poll_id>/delete/', views.polls_delete, name='delete_poll'),
    path('poll/<int:poll_id>/end/', views.endpoll, name='end_poll'),
    path('poll/<int:poll_id>/edit/choice/add/', views.add_choice, name='add_choice'),
    path('poll/choice/<int:choice_id>/edit/', views.choice_edit, name='choice_edit'),
    path('choice/<int:choice_id>/delete/',
         views.choice_delete, name='choice_delete'),
    path('poll/<int:poll_id>/', views.poll_detail, name='detail'),
    path('poll/<int:poll_id>/vote/', views.poll_vote, name='vote'),
    path('poll/<int:poll_id>/results/', views.poll_vote, name='poll_results'),
    path('poll/add/', views.polls_add, name = 'add')
]