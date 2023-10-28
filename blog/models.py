from django.db import models

# Create your models here.

class Post(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=30)
    description = models.TextField()
    picture = models.ImageField(upload_to="post/")
    profile = models.ImageField(upload_to="profile/")

class Comment(models.Model):
    user_name = models.CharField(max_length=30)
    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)