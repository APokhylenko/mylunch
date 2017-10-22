from django.db import models
from django.core.mail import send_mass_mail
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Product(models.Model):
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=30)
    price = models.IntegerField()

    def __str__(self):
        return self.name