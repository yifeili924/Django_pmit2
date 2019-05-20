# Generated by Django 2.0.6 on 2018-06-18 13:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Agency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BedTypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('bedtype', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('country_code', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=200)),
                ('picture', models.CharField(max_length=200)),
                ('link', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoomMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('agency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Agency')),
                ('resort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Resort')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=200)),
                ('resort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Resort')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('checkin', models.DateField()),
                ('checkout', models.DateField()),
                ('adults', models.PositiveSmallIntegerField()),
                ('kids', models.PositiveSmallIntegerField()),
                ('kids_ages', models.CharField(max_length=200)),
                ('original_price', models.CharField(max_length=200)),
                ('current_price', models.CharField(max_length=200)),
                ('reservation_number', models.CharField(max_length=50)),
                ('notes', models.CharField(max_length=500)),
                ('discount', models.SmallIntegerField(default=25, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)])),
                ('bedtype', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='trips.BedTypes')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('resort', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.Resort')),
                ('roomtype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.RoomType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='roommapping',
            name='resort_roomtype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.RoomType'),
        ),
    ]
