from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager as DjangoUserManager
from django.db import models


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
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return f"Пользователь [Email: {self.email}, Telegram: {self.telegram_user_id}]"


class Application(BaseModel):
    trademark = models.FileField(upload_to="trademarks/", null=True, blank=True, verbose_name="Товарный знак")

    phone_number = models.CharField(max_length=20, null=False, verbose_name='Телефон')
    person_name = models.CharField(max_length=100, null=True, verbose_name='Имя')
    description = models.CharField(max_length=1000, null=True, verbose_name='Описание')

    is_check_trademark = models.BooleanField(verbose_name="Проверка знака")
    is_done = models.BooleanField(verbose_name="Заявка выполнена")

    class Meta:
        unique_together = [('phone_number', 'person_name', 'description')]
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return f"Заявка [Имя: {self.person_name}, Телефон:{self.phone_number}]"


class SolvedApplication(BaseModel):
    title = models.CharField(max_length=35, null=False, verbose_name="Заголовок")
    history = models.TextField(null=False, verbose_name="История")
    result = models.TextField(null=False, verbose_name="Итог")

    class Meta:
        verbose_name = 'Решённая задача'
        verbose_name_plural = 'Решённые задачи'

    def __str__(self):
        return f"Решённая задача: {self.title}"

