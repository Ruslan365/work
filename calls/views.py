from __future__ import print_function
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from calls.start import event_creator
from users.models import User
from posts.models import Post


@login_required
def search_call(request):
    queryset = User.objects.birthdays()
    recent_posts = Post.objects.filter(is_published=1)[:5:]
    if not request.user.is_superuser:
        return HttpResponseRedirect(reverse('accounts:home_page'))

    if 'tags' in request.GET:
        emails_dict = []
        emails_buf = dict()
        y = 0
        x1 = 0
        query_row = request.GET.get('tags')
        partydate = request.GET.get('partydate')
        room = request.GET.get('room')
        query = query_row.split(', ')
        del query[len(query) - 1]
        for x in query:
            emails_buf = dict(email='')
            emails_dict.append(emails_buf)
            y += 1
        y = 0
        for z in emails_dict:
            z["email"] = query[y]
            y += 1
        event_creator(emails_dict, partydate, room)
    emails = User.objects.values_list("email", flat=True)
    print(emails)
    return render(
        request,
        "../templates/intranet/home/conference.html",
        {
            "user_emails": emails,
            "birthdays": queryset,
            "recent_posts": recent_posts
        },
    )
