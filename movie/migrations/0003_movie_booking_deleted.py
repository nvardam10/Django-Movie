# Generated by Django 4.2.4 on 2023-08-15 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0002_alter_movie_booking_movieid_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie_booking',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
