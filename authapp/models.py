from django.db import models
from django.contrib.auth.models import AbstractUser



class ShopUser(AbstractUser):
    age = models.PositiveIntegerField(verbose_name='Возраст', default=18)
    is_active = models.BooleanField(verbose_name='активность', default=True)



