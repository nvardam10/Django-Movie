# Generated by Django 4.2.4 on 2023-08-11 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_moviebooking_bookingid'),
    ]

    operations = [
        migrations.AddField(
            model_name='moviebooking',
            name='UserID',
            field=models.IntegerField(default=1, unique=True),
        ),
    ]
