import uuid
from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name="profile")
    otp =models.CharField(max_length=6,null=True,blank=True)
    mobnumber= models.CharField(max_length=20)
    uid =models.UUIDField(default=uuid.uuid4)