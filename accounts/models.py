from django.db import models
from django.contrib.auth.models import User
import uuid
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.user.username