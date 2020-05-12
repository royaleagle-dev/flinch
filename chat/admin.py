from django.contrib import admin
from chat.models import Chat, Contact, Notification

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'contact')

admin.site.register(Chat)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Notification)

