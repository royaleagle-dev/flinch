from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
import datetime
import uuid

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete = models.CASCADE)
	phone = models.CharField(max_length = 20)
	location = models.CharField(max_length = 255, default = 'Ijebu-Ode, Ogun State, Nigeria')

	@receiver(post_save, sender = User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user = instance)

	@receiver(post_save, sender = User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()

	def __str__(self):
		return '{0} | {1}'.format(self.phone, self.user.username)


