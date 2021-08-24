from django.urls import path
from posts import views as post_views
from users import views as user_views
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from calls import views as calls_views
from posts.models import Post, Comment, LikeDislike
app_name = "intranet"
urlpatterns = [
    path("search/", post_views.post_search, name="search_results"),
    path("dir/", calls_views.search_call, name="dir"),
    path("list/", post_views.post_list_main, name="post_list"),
    path('post/<int:pk>/', post_views.post_detail, name = 'post_detail'),
    path("", post_views.home_page, name="home_page"),
    path('comment/<int:pk>/', post_views.comment_page, name="comment_page"),
    path("organization/", user_views.organization_page),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", user_views.logout_view, name="logout"),
    path("profile/dge<id>du/", post_views.profile_page, name="user_profile"),
    path("profile/dge<id>du/creator/", post_views.post_creator, name="post_creator"),
    path("profile/dge<id>du/editor/", user_views.profile_redactor, name="profile_redactor"),
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
    path(
        "reset_password/",
        auth_views.PasswordResetView.as_view(template_name="../templates/registration/password_reset.html"),
        name="reset_password",
    ),
    path(
        "password_reset/done/",
        auth_views.PasswordResetDoneView.as_view(template_name="../templates/registration/password_reset_sent.html"),
        name="password_reset_done",
    ),
    path(
        "reset/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(template_name="../templates/registration/password_reset_form.html"),
        name="password_reset_confirm",
    ),
    path(
        "reset_password_complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="../templates/registration/password_reset_complete.html"
        ),
        name="password_reset_complete",
    ),
]
