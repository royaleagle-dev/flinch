from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView
from chat.models import Chat, Contact, Notification
from django.contrib.auth.models import User
import datetime
import re
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone

from hashlib import md5
# Create your views here.

def deleteContact(request, username):
    idList = [ ]
    myContact = Contact.objects.filter(user__username__exact = request.user.username).filter(contact__exact = username)
    friendContact = Contact.objects.filter(user__username__exact = username).filter(contact__exact = request.user.username)
    for items in myContact:
        idList.append(items.id)
    for items in friendContact:
        idList.append(items.id)
    print(idList)
    for items in idList:
        x = get_object_or_404(Contact, id = items)
        x.delete()
    messages.success(request, "contact successfully deleted")
    return redirect('chat:chatIndex')

def chatRoom(request, receiver):
    chats = Chat.objects.filter(key__contains = request.user.username).filter(key__contains = receiver).order_by('-id')
    return render(request, 'chat/chatRoom.html', {'chats':chats})

def chatIndex(request):
    
    user = request.user
    users = User.objects.all().order_by('-id')
    contacts = Contact.objects.filter(contact__exact = request.user.username)
    notificationCount = Notification.objects.filter(user__username__exact = request.user.username).filter(status__exact = 'u').count()
    notifications = Notification.objects.filter(user__username__exact = request.user.username).order_by('-id')
    
    ctx = {
        'user':user,
        'users':users,
        'contacts':contacts,
        'notificationCount':notificationCount,
        'notifications':notifications,
    }
    return render(request, 'chat/chatIndex.html', ctx)

def addContact(request):
    contact = request.GET.get('addContactByEmail')
    
    #Verify contact is in Data base
    users = User.objects.all()
    status = 'absent'
    for user in users:
        if user.username == contact:
            status = 'present'
    
    if status == 'present':
        #On my Contact List
        myList = Contact(user = request.user, contact = contact)
        #On my Friend's list
        friendList = Contact(user = User.objects.get(username = contact), contact = request.user.username)
        
        #saving entries
        myList.save()
        friendList.save()
        
        #Notifying Users
        myNotification = Notification(user = request.user, contact = contact, body = "You have successfully added {0} to your contact list".format(contact))
        friendNotification = Notification(user = User.objects.get(username = contact), contact = request.user.username, body = "You have been added to {0}'s contact list ".format(request.user.username))
        
        #save notification
        myNotification.save()
        friendNotification.save()
        
        messages.success(request, 'Contact Successfully added')
        return redirect ('chat:chatIndex')
    else:
        messages.warning(request, 'Contact not yet registered')
        return redirect('chat:chatIndex')

def startChat(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        sender = request.POST.get('sender')
        receiver = request.POST.get('receiver')
        key = request.POST.get('key')
        
        chat = Chat(sender = sender, receiver = receiver, key = key, message = message)
        notif = Notification(user = User.objects.get(email=receiver), contact = request.user.username, body = "You've just received a message from {0}".format(sender))
        
        chat.save()
        notif.save()
        return HttpResponse('successfuly sent message')
        
        
    