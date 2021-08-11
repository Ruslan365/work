from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models
from datetime import datetime
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
# from imagekit.processors import ResizeToFit, Adjust, ResizeToFill
# from imagekit.models.fields import ImageSpecField
from django.utils import timezone
from django.contrib.humanize.templatetags.humanize import naturaltime


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

    def is_online(self):
        if self.last_login_at:
            return (timezone.now() - self.last_login_at) < timezone.timedelta(minutes=15)
        return False
    #
    # def upcoming_birthday(self):
    #     if self.birth_date



class User(AbstractBaseUser, PermissionsMixin):  # abstract user только почта и пароль
    avatar = models.ImageField(
        default="default.jpg",
        upload_to="profile_pics",
    )
    email = models.EmailField(unique=True, default="")
    password = models.CharField(max_length=128)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login_at = models.DateTimeField(blank=True, null=True)
    objects = UserManager()
    birth_date = models.DateField(blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    is_staff = models.BooleanField("staff status", default=False)
    is_active = models.BooleanField(default=True)
    about = models.TextField(blank=True)
    twitter_id = models.CharField('https://twitter.com/',max_length=255, blank=True, null=True)
    facebook_id = models.CharField('https://facebook/public/',max_length=255, blank=True, null=True)
    def is_online(self):
        if self.last_login_at:
            return (timezone.now() - self.last_login_at) < timezone.timedelta(minutes=10)
        return False

    @property
    def age(self):
        return int((datetime.now().date().year - self.birth_date.year))+1


    @property
    def get_email(self):
        return self.email

    def __str__(self):
        return f"User {self.email}"


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="children")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}"


class SocialNetwork(models.Model):

    user = models.ForeignKey(User, default="", related_name="social_network", on_delete=models.CASCADE)
    social_network_name = models.TextField(max_length=32, blank=True)
    social_network_link = models.TextField(max_length=128)

    def __str__(self):
        return f"{User} social networks"
