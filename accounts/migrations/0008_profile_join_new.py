# Generated by Django 2.2.7 on 2020-06-16 19:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200615_2051'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='join_new',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='وقت الانضمام :'),
            preserve_default=False,
        ),
    ]
