from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, RegexValidator
from django.db import models


class User(AbstractUser):
    pass


class Speciality(models.Model):
    name = models.CharField(max_length=50)


class Doctor(User):
    license_number = models.CharField(
        max_length=6,
        unique=True,
        validators=[MinLengthValidator(6)],
    )
    phone = models.CharField(
        max_length=8,
        validators=[RegexValidator(r'^\d{8}$', "Le téléphone doit contenir 8 chiffres.")],
    )
    specialities = models.ManyToManyField(Speciality, related_name='doctors', blank=True)


class Patient(User):
    national_id = models.CharField(
        max_length=8,
        unique=True,
        validators=[RegexValidator(r'^\d{8}$', "Le CIN doit contenir exactement 8 chiffres.")],
    )
    phone = models.CharField(
        max_length=8,
        validators=[RegexValidator(r'^\d{8}$', "Le téléphone doit contenir 8 chiffres.")],
    )
    birth_date = models.DateField()