from django.contrib import admin
from chat.models import Msg, Friend, Chat

# Register your models here.

admin.site.register(Msg)
admin.site.register(Friend)
admin.site.register(Chat)

