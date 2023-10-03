from django.db import models

# Create your models here.

class comment(models.Model):
    user_name = models.CharField(max_length=30)
    body = models.TextField()