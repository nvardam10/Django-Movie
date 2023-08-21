# Generated by Django 4.2.4 on 2023-08-15 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_movie_booking_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_booking',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='movie_booking',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='movie_details',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='movie_details',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user_details',
            name='date_updated',
            field=models.DateField(auto_now=True),
        ),
    ]
