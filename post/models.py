from django.db import models

class Post(models.Model):
    video = models.FileField(upload_to='videos/')
    caption = models.TextField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)