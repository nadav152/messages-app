from django.db import models
from django.contrib.auth.models import User
import logging

# Create your models here.


class Message(models.Model):

    sender = models.ForeignKey(User, null=True , db_index=True,on_delete=models.SET_NULL, related_name='sender')
    receiver = models.ForeignKey(User, null=True , db_index=True,on_delete=models.SET_NULL, related_name='receiver')
    message = models.TextField(default='')
    subject = models.CharField(
        max_length=128, db_index=True, default='none', unique=True
    )
    creation_time = models.DateTimeField(auto_now_add=True, db_index=True)
    

class MessageToUser(models.Model):
    receiver = models.ForeignKey(
        User, db_index=True, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, db_index=True, on_delete=models.CASCADE)
    creation_time = models.DateTimeField(auto_now_add=True)
    was_seen = models.BooleanField(default=False)
    

