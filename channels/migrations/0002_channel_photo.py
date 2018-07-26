# Generated by Django 2.0.7 on 2018-07-26 22:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('channels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='channel',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='channel_image'),
            preserve_default=False,
        ),
    ]
