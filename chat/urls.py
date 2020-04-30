from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.ChatIndex, name = 'chatIndex'),
    path('addFriend/', views.addFriend, name = 'addFriend'),
    #path('sendMsg/', views.sendMsg, name = 'sendMsg'),
    path('chatRoom/<str:username>', views.chatRoom, name = 'chatRoom'),
    path('test/', views.test, name = 'test'),
    path('acceptFriend/<str:friend>/', views.acceptFriend, name = 'acceptFriend'),
    path('declineFriend/<int:id>/', views.declineFriend, name = 'declineFriend'),
]