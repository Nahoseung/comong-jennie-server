from django.db import models
# from User.model import User
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    # author= User
    # tag = models.CharField(max_length=10)
    # likes = 
    dt_created = models.DateTimeField(verbose_name="Date Created",auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name="Date Modified",auto_now=True)


class Board(models.Model):
    grade = models.IntegerField()
    sub = models.CharField(max_length=20)
    profs = models.CharField(max_length=10)


