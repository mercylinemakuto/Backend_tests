from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class Supplier(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    phone_number = models.CharField(max_length = 15)
    created_at = models.DateField(auto_now_add = True)

    def __str__(self):
        return self.user.get_full_name()