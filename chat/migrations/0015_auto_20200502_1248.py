# Generated by Django 2.2.7 on 2020-05-02 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_auto_20200502_0355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='email',
            new_name='contact',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='location',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='registered',
        ),
    ]
