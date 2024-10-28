from django.db import models

# Create your models here.
# models.py
from django.db import models
from django.utils import timezone
# blog/models.py
from django.db import models

class BlogPost(models.Model):
    title = models.CharField(max_length=2000)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
