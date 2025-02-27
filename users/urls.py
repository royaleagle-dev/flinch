from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.userReg, name = 'userReg'),
	path('userLogin/', views.userLogin, name = 'userLogin'),
	path('userSignup/', views.userSignup, name = 'userSignup'),
	path('userLogout/', views.userLogout, name = 'userLogout'),
]