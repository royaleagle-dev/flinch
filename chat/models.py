from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.

class Msg(models.Model):
    sender = models.EmailField()
    message = models.CharField(max_length = 50000)
    receiver = models.EmailField()
    state = (
    ('r', 'read'),
    ('u', 'unread'),
    )
    status = models.CharField(max_length = 1, choices = state, default = 'u')
    timestamp = models.DateTimeField()
    
    def __str__(self):
        return self.sender

class Friend(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    friend = models.CharField(max_length = 2000)
    timestamp = models.DateField(default = str(datetime.datetime.now().date()))
    state =(
    ('p', 'pending'),
    ('a', 'accepted'),
    ('d', 'declined'),
    )
    status = models.CharField(max_length = 1, choices = state, default = 'p')
    modes = (
    ('r', 'received'),
    ('s', 'sent'),
    )
    mode = models.CharField(max_length = 1, choices = modes, default = 's')
    
    def __str__(self):
        return self.friend
    
class Chat(models.Model):
    sender = models.CharField(max_length = 255)
    receiver = models.CharField(max_length = 255)
    chat = models.TextField(max_length = 100000)
    timestamp = models.DateTimeField()
    modes = (
    ('s','send'),
    ('r', 'receive'))
    mode = models.CharField(max_length = 1, default = 's', choices = modes)
    key = models.CharField(max_length = 255)
    
    def __str__(self):
        return self.chat
    


