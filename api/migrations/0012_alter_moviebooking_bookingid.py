# Generated by Django 4.2.4 on 2023-08-11 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_moviebooking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moviebooking',
            name='BookingID',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
