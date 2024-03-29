from datetime import datetime
from datetime import timedelta, date
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models import Q


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

    def birthdays(self):
        today = date.today()
        fifteen_days = today + timedelta(days=15)
        if today.month == fifteen_days.month:
            return super().get_queryset().filter(
                Q(birth_date__month=today.month, birth_date__day__gte=today.day) & Q(
                    birth_date__day__lte=fifteen_days.day)
            )
        else:
            return super().get_queryset().filter(
                Q(birth_date__month=today.month, birth_date__day__gte=today.day) |
                Q(birth_date__month=fifteen_days.month, birth_date__day__lte=fifteen_days.day)
            )


class User(AbstractUser):
    username = None
    avatar = models.ImageField(
        default="default.jpg",
        upload_to="profile_pics",
    )
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    role = models.CharField(max_length=30, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_login_at = models.DateTimeField(blank=True, null=True)
    objects = UserManager()
    birth_date = models.DateField(blank=True, null=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    about = models.TextField(blank=True)
    twitter_id = models.CharField('https://twitter.com/', max_length=255, blank=True, null=True)
    facebook_id = models.CharField('https://facebook/public/', max_length=255, blank=True, null=True)
    objects = UserManager()
    # social_media = models.ManyToManyField(SocialMedia, related_name="social_medias", blank=True)


    def __str__(self):
        return f"User {self.email}"


    def age(self):
        return  date.today().year - self.birth_date.year + 1

