# Generated by Django 4.2 on 2023-05-20 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediaid_app', '0009_remove_buddy_user_buddy_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='msg_receiver',
        ),
        migrations.RemoveField(
            model_name='chat',
            name='msg_sender',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='friends',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Buddy',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
