'''
from django.db import models
from django.utils import timezone
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.base_user import BaseUserManager
from django.urls import reverse

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        User creator
        """
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)

        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):  # abstract user только почта и пароль
    avatar = models.ImageField(null=True, blank=True)
    email = models.EmailField(unique=True, default="")
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    is_staff = models.BooleanField("staff status", default=False)
    is_active = models.BooleanField(default=True)
    about = models.TextField(blank=True)

    @property
    def get_email(self):
        return self.email

    def __str__(self):
        return f"User {self.email}"

class LikeDislike(models.Model):

    LIKE = 1
    DISLIKE = -1
    VOTES = (("LIKE", "НРАВИТСЯ"), ("DISLIKE", "НЕ НРАВИТСЯ"))

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vote = models.SmallIntegerField(choices=VOTES)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()


class LikeDislikeManager(models.Manager):
    use_for_related_fields = True

    def likes(self):
        return self.get_queryset().filter(LikeDislike.vote > 0).count()

    def dislikes(self):
        return self.get_queryset().filter(LikeDislike.vote < 0).count()


class PublishManager(models.Manager):
    def get_queryset(self):
        return super(PublishManager, self).get_queryset().filter(is_published="1")


class Post(models.Model):

    STATUS_CHOICES = (("0", "Not Published"), ("1", "Published"))
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="")
    # author_avatar = models.ImageField(default="default.jpg")
    title = models.CharField(max_length=250)
    # title_image = models.ImageField()
    body = models.CharField(max_length=10000, default="")
    tags = models.CharField(max_length=250, default="")
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.CharField(max_length=1, choices=STATUS_CHOICES, default="0")
    like = GenericRelation(LikeDislike)
    dislike = GenericRelation(LikeDislike)
    slug = models.SlugField(max_length=250, unique_for_date="created_at", default="")
    published = PublishManager()

    def get_absolute_url(self):
        return reverse(
            "intranet:post_detail",
            args=[self.published_at.year, self.published_at.month, self.published_at.day, self.slug],
        )

    def __str__(self):
        return f"Post {self.title} by {self.author}, Post_id:{self.id}"


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default="1")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments", default="", null=True)
    # author_avatar = models.ImageField(default="", height_field=30, width_field=30)
    # image = models.ImageField()
    body = models.TextField(default="")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    like = GenericRelation(LikeDislike)
    dislike = GenericRelation(LikeDislike)
    reply = models.ForeignKey("self", null=True, related_name="replies", on_delete=models.CASCADE)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"


class Tag(models.Model):

    tag = models.CharField(max_length=64, default="")
    tag_item = models.ManyToManyField(Post)


class TagManager(models.Manager):
    def seek(self, *args):
        query_set1 = self.get_queryset().filter(tag = f'{args[0]}')
        for element in args[1::]:
            query_set2 = self.get_queryset().filter(tag = f'{element}')
            query_set1 = query_set1 & query_set2
        return query_set1

class SocialNetwork(models.Model):

    user = models.ForeignKey(User, default="", related_name="social_network", on_delete=models.CASCADE)
    social_network_name = models.TextField(max_length=32, blank=True)
    social_network_link = models.TextField(max_length=128)
'''