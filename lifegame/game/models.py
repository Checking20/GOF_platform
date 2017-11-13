from django.db import models

# Create your models here.

class GUser(models.Model):
    User_name = models.CharField(max_length=32, null=False)
    Password = models.CharField(max_length=32, null=False)
    Map_ID = models.BigIntegerField(null=False)

class GMap(models.Model):
    Map_ID = models.BigIntegerField(primary_key=True, null=False)
    Col = models.IntegerField(null=False)
    Row = models.IntegerField(null=False)
    Content = models.CharField(max_length=255, null=False)

class State(models.Model):
    User_name = models.CharField(max_length=32, null=False)
    Map_ID = models.BigIntegerField(null=False)
    Like = models.IntegerField(null=False, default=0)
    Commentno = models.IntegerField(null=False, default=0)
    Read = models.IntegerField(null=False, default=0)
    Timestamp = models.DateTimeField(auto_now=True)
    Feeling = models.CharField(max_length=32, null=True)

class Comment(models.Model):
    State_ID = models.IntegerField(null=False)
    Comment_User_name = models.CharField(max_length=32, null=False)
    content = models.CharField(max_length=255, null=False)
    IsMap = models.BooleanField(null=False)