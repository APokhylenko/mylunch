from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail


from order.models import Product


class User(AbstractUser):
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField(max_length=20, blank=True)
    REQUIRED_FIELDS = ['email']
    order = models.ManyToManyField(Product)

    def save(self, *args, **kwargs):
        emails_passwords = {}
        if not self.username:
            self.username = self.email
        if not self.password:
            password = User.objects.make_random_password(length=6)
            self.password = make_password(password)
            emails_passwords.update({self.email: password})
            send_mail('MyLunch - Ваш пароль', password, 'from@example.com',
                  [self.email], fail_silently=False)
        super(User, self).save(*args, **kwargs)

