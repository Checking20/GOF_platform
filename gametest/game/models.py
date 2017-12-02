from django.db import models

# Create your models here.

class GUser(models.Model):
    User_name = models.CharField(max_length=32, null=False)
    Password = models.CharField(max_length=32, null=False)

    def __str__(self):
        return self.User_name

class GMap(models.Model):
    Map_ID = models.BigIntegerField(primary_key=True, null=False)
    Content = models.CharField(max_length=255, null=False)
    User_name = models.CharField(max_length=32, null=False)
    map_description = models.CharField(max_length=64, null=True)
    map_name = models.CharField(max_length=32, null=True)
    Createtime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Createtime

class State(models.Model):
    User_name = models.CharField(max_length=32, null=False)
    Map_ID = models.BigIntegerField(null=False)
    Like = models.IntegerField(null=False, default=0)
    Read = models.IntegerField(null=False, default=0)
    Timestamp = models.DateTimeField(auto_now=True)
    Description = models.CharField(max_length=64, null=True)
    State_name = models.CharField(max_length=32, null=True)

    def __str__(self):
        return self.State_name

class Comment(models.Model):
    State_ID = models.IntegerField(null=False)
    Comment_User_name = models.CharField(max_length=32, null=False)
    content = models.CharField(max_length=255, null=False)
    Createtime = models.DateTimeField(auto_now=True)
    IsMap = models.BooleanField(null=False)

    def __str__(self):
        return self.Comment_User_name