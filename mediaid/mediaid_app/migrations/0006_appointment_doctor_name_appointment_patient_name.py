# Generated by Django 4.2 on 2023-05-18 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mediaid_app', '0005_appointment'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='doctor_name',
            field=models.CharField(default='abc', max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient_name',
            field=models.CharField(default='abc', max_length=30),
            preserve_default=False,
        ),
    ]
