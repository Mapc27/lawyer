from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager as DjangoUserManager
from django.db import models
from django.core.validators import RegexValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


class UserManager(DjangoUserManager):
    def create_user(self, username, password=None, **extra_fields):
        user = self.model(email=username)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email=None, password=None, **extra_fields):
        user = self.model(email=email, is_staff=True, is_superuser=True)
        user.set_password(password)
        user.save()
        return user


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    USERNAME_FIELD = "email"

    email = models.EmailField(unique=True, verbose_name="Email")
    password = models.CharField(max_length=128, verbose_name="Пароль")
    is_staff = models.BooleanField(default=False)
    telegram_user_id = models.PositiveIntegerField(verbose_name="Telegram user ID", null=True, blank=True)

    class Meta:
        verbose_name = "пользователь"
        verbose_name_plural = "пользователи"


class Application(BaseModel):
    phone_validator = RegexValidator(regex="^(\+7|8|)([0-9]{10})$",
                                     message="Phone number incorrect")

    phone_number = models.CharField(validators=[phone_validator], max_length=16)
    person_name = models.CharField(max_length=100)
    description = models.TextField()
    is_notified = models.BooleanField(default=False)

    class Meta:
        unique_together = [('phone_number', 'person_name', 'description')]


class SolvedApplication(BaseModel):
    title = models.CharField(max_length=100)
    history = models.TextField()
    result = models.TextField()
