from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class BlogPost(models.Model):

    # Create fields for post title, text, time of publish
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=128)
    post_text = models.TextField()
    # Auto add date/time of publish
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post_title
