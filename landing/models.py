from distutils.command.upload import upload
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=32)
    content = models.TextField()
    head_image = models.ImageField(
        upload_to = "landing/images/%Y/%m/%d/%H/",
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phonenumber = models.TextField(null=True)
    read_book = models.TextField(null=True)

    def __str__(self):
        return f"title: {self.title}"