# Generated by Django 4.2 on 2023-10-16 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediaid_app', '0015_alter_appointment_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comission',
            name='percentage',
            field=models.CharField(default='5', max_length=20),
            preserve_default=False,
        ),
    ]
