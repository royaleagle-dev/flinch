from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    contact = models.EmailField(max_length = 255)
    
    def __str__(self):
        return self.user.username
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    contact = models.EmailField(max_length = 255)
    body = models.CharField(max_length = 2000, default = '')
    timestamp = models.DateTimeField(auto_now_add = True)
    choices = (
        ('r', 'read'),
        ('u', 'unread'),
    )
    status = models.CharField(max_length = 1, choices = choices, default = 'u')
    
    def __str__(self):
        return self.body
    
class Chat(models.Model):
    sender = models.EmailField(max_length = 255)
    receiver = models.EmailField(max_length = 255)
    key = models.CharField(max_length = 255)
    message = models.TextField(max_length = 5000)
    timestamp = models.DateTimeField(auto_now_add = True)\
    
    def __str__(self):
        return self.sender