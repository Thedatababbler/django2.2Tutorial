from django.db import models

# Create your models here.

# creat fields to database
class BlogPost(models.Model):
    title = models.TextField()
    content = models.TextField(null=True, blank=True)

# run manage.py makemigrations and manage.py migrate everytime
# you change the models

