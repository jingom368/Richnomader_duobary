from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phonenumber = models.TextField(null=True)
    read_book = models.TextField(null=True)
