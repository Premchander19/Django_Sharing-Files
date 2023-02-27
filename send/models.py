from django.db import models
from django.contrib.auth.models import User, auth


# Create your models here.
class Data(models.Model):
    username = models.TextField(max_length=25, default=0)
    file = models.FileField(upload_to='Receive', blank=True, null=True)
    text = models.TextField(max_length=25, default=0)
    Date = models.DateField(auto_now_add=True)
    Time = models.TextField(null=True, max_length=5)
    Expired = models.TextField(null=True, max_length=5)

    # def __str__(self):
    #    return self.text
