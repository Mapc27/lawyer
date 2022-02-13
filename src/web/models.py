from django.db import models
from django.core.validators import RegexValidator


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


class Application(BaseModel):
    phone_validator = RegexValidator(regex="^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$",
                                     message="Phone number incorrect")

    phone_number = models.CharField(validators=[phone_validator], max_length=16)
    person_name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        unique_together = [('phone_number', 'person_name', 'description')]


class SolvedApplication(BaseModel):
    title = models.CharField(max_length=100)
    history = models.TextField()
    result = models.TextField()
