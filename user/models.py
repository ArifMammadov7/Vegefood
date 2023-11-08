from django.db import models
# from django.utils.translation import gettext as _ Sultan silib burdada obirsi modelsdə də

from django.contrib.auth.models import AbstractUser


class BaseUser(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    picture = models.ImageField(upload_to='users', blank=True)

    class Meta:
        verbose_name=("User")
        verbose_name_plural=("Users")

    def __str__(self):
        return self.username