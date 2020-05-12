from django.urls import path
from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.chatIndex, name = 'chatIndex'),
    path('addContact/', views.addContact, name = 'addContact'),
    path('startChat/', views.startChat, name = 'startChat'),
    path('chatRoom/<str:receiver>/', views.chatRoom, name = 'chatRoom'),
    path('delContact/<str:username>/', views.deleteContact, name = 'deleteContact'),
]