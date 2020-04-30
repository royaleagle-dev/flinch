from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from chat.models import Msg, Friend, Chat
from django.contrib.auth.models import User
import datetime
import re
from django.contrib import messages
from django.http import HttpResponse
from django.utils import timezone

from hashlib import md5
# Create your views here.

def test(request):
    return render(request, 'chat/test.html')

def ChatIndex(request):
    username = request.user.username
    
    allMsg = Chat.objects.filter(key__contains = request.user.username).order_by('-id')[:5]
    
    friends = Friend.objects.filter(mode__exact = 's').filter(friend__exact = request.user.username).filter(status__exact = 'p')
    
    acceptedFriend = Friend.objects.filter(friend__exact = request.user.username).filter(status__exact = 'a')
    ctx = {
        'allMsg':allMsg,
        'friends':friends,
        'acceptedFriend':acceptedFriend,
    }
    return render(request, 'chat/chatIndex.html', ctx)

def addFriend(request):
    search = request.GET.get('search')
    pattern = re.compile (r'^(\D{11})(\D{1})')
    x = re.sub(pattern, '', search)
    opp = User.objects.get(email = x)
    users = User.objects.all()
    USERS = set()
    for item in users:
        USERS.add(item.username)
        messages.success(request, USERS)
    
    if x in USERS:
        date = str(datetime.datetime.now().date())
        messages.success(request, 'User is present')
        
        friend = Friend(user = request.user, friend = x, timestamp = str(date), status = 'p', mode = 's')
        
        oppFriend = Friend(user = opp, friend = request.user.username, timestamp = str(date), status = 'p', mode = 'r')
        oppFriend.save()
        friend.save()
        return HttpResponse('success')
    
def chatRoom(request, username):
    if request.method == 'POST':
        me = request.POST.get('me'),
        friend = request.POST.get('friend')
        message = request.POST.get('message')
        key = request.POST.get('key')
        message = re.sub('^f_send ', '', message)
        chat = Chat(sender = request.user.username, receiver = friend, chat = message, timestamp = timezone.now(), mode = 's', key = str(request.user.username)+str(friend))
        chat.save()
        messages.success(request, 'Chat successfully added')
        return HttpResponse('Success')
    
    user = User.objects.get(email = request.user.username)
    me = user.username
    friend = User.objects.get(email = username)
    Friend = friend.username
    print (Friend)
    key = str(me)+str(friend)
    chat = Chat.objects.filter(key__icontains = request.user.username).filter(key__icontains = Friend).order_by('-id')
    ctx = {
        'me':me,
        'Friend':Friend,
        'chat':chat,
    }
    return render(request, 'chat/chatRoom.html', ctx)


def acceptFriend(request, friend):
    user = request.user.username
    friendRequest = Friend.objects.filter(status__exact = 'p')
    for item in friendRequest:
        if item.user.username == request.user.username and item.friend == friend:
            item.status = 'a'
            item.save()
        if item.user.username == friend and item.friend == request.user.username:
            item.status = 'a'
            item.save()
    return redirect('chat:ChatIndex')
    
    
def declineFriend(reqeust, friend):
    user = request.user.username
    friendRequest = Friend.objects.filter(status__exact = 'p')
    for item in friendRequest:
        if item.user.username == request.user.username and item.friend == friend:
            item.delete()
        if item.user.username == friend and item.friend == request.user.username:
            item.delete()
    return redirect('chat:ChatIndex')
    
    
    