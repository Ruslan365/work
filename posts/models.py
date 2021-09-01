from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from users.models import User
from django.db.models import Sum

class Tag(models.Model):

    name = models.CharField(max_length=30, default="")


    def __str__(self):
        return f"{self.name}"


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        # Забираем queryset с записями больше 0
        return self.get_queryset().filter(vote__gt=0)

    def dislikes(self):
        # Забираем queryset с записями меньше 0
        return self.get_queryset().filter(vote__lt=0)

    def sum_rating(self):
        # Забираем суммарный рейтинг
        return self.get_queryset().aggregate(Sum('vote')).get('vote__sum') or 0

    def articles(self):
        return self.get_queryset().filter(content_type__model='article').order_by('-articles__pub_date')

    def comments(self):
        return self.get_queryset().filter(content_type__model='comment').order_by('-comments__pub_date')

    def total_comments(self):
        return self.get_queryset().filter(content_type__model='comment').count()


class LikeDislike(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE, 'Не нравится'),
        (LIKE, 'Нравится')
    )

    vote = models.SmallIntegerField(verbose_name="Голос", choices=VOTES)
    user = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    objects = LikeDislikeManager()


class Post(models.Model):

    STATUS_CHOICES = (("0", "Not Published"), ("1", "Published"))
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    preview_pic = models.ImageField(blank=True, upload_to="post_preview_pics")
    author_avatar = models.ImageField(default="default.jpg")
    title = models.CharField(max_length=255)
    description = models.TextField(default="", max_length=255)
    body = models.TextField(default="")
    created_at = models.DateTimeField(default=timezone.now)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.CharField(max_length=1, choices=STATUS_CHOICES, default="0")
    slug = models.SlugField(max_length=250, unique_for_date="created_at", default="")
    objects = models.Manager()
    tag = models.ManyToManyField(Tag, related_name="tags", blank=True)
    votes = GenericRelation(LikeDislike, related_query_name="posts")
    post_views = models.IntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/post/{self.pk}/'

    def __str__(self):
        return f"Post {self.title} by {self.author}"

    def get_date(self):
        return self.published_at.strftime('%B %d, %Y')


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments", default="", null=True
    )
    body = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    votes = GenericRelation(LikeDislike, related_query_name="comments")
    reply = models.ForeignKey(
        "self", null=True, related_name="replies", on_delete=models.CASCADE, blank=True,
    )

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/post/{self.post.pk}/comment/{self.pk}'

    def get_date(self):
        return self.created_at.strftime('%B %d, %Y')
