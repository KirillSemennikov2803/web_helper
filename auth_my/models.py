from django.db import models


# Create your models here.

class Users(models.Model):
    login = models.CharField(max_length=36, unique=True)
    password_hash = models.CharField(max_length=50)


class Notes(models.Model):
    user_id = models.ForeignKey('Users', related_name='users_to_notes', on_delete=models.CASCADE)
    date = models.DateTimeField()
    text = models.TextField()


class Notifications(models.Model):
    user_id = models.ForeignKey('Users', related_name='users_to', on_delete=models.CASCADE)
    date = models.DateTimeField()
    text = models.TextField()
