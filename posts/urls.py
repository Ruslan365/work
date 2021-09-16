from django.contrib.auth.decorators import login_required
from django.urls import path

from posts import views as post_views
from posts.models import Post, Comment, LikeDislike

app_name = "posts"
urlpatterns = [
    path("search/", post_views.post_search, name="search_results"),
    path("list/", post_views.post_list, name="post_list"),
    path('post/<int:pk>/', post_views.post_detail, name='post_detail'),
    path("", post_views.home_page, name="home_page"),
    path('comment/<int:pk>/', post_views.comment_page, name="comment_page"),
    # path("profile/dge<id>du/creator/", post_views.post_creator, name="post_creator"),
    path('post/<int:pk>/like/',
         login_required(post_views.VotesView.as_view(model=Post, vote_type=LikeDislike.LIKE)),
         name='post_like'),
    path('post/<int:pk>/dislike/',
         login_required(post_views.VotesView.as_view(model=Post, vote_type=LikeDislike.DISLIKE)),
         name='article_dislike'),
    path('comment/<int:pk>/like/',
         login_required(post_views.VotesView.as_view(model=Comment, vote_type=LikeDislike.LIKE)),
         name='comment_like'),
    path('comment/<int:pk>/dislike/',
         login_required(post_views.VotesView.as_view(model=Comment, vote_type=LikeDislike.DISLIKE)),
         name='comment_dislike'),
    path("tag=<str:tag>/", post_views.tag_page, name="tag_page"),
]
