# Generated by Django 2.0.6 on 2018-06-25 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trips', '0007_remove_trip_kids_ages'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='kids_ages',
            field=models.CharField(max_length=25, null=True),
        ),
    ]
