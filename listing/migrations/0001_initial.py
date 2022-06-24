# Generated by Django 4.0.5 on 2022-06-23 10:25

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='NeighborHood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('location', models.CharField(max_length=50, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('occupants', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('Profile_photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('Bio', models.TextField(max_length=50, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('email_address', models.CharField(max_length=50, null=True)),
                ('business', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to='listing.business')),
                ('neighborhood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='neighbourhood', to='listing.neighborhood')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50)),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('description', models.TextField(max_length=50, null=True)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('neighborHood', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='listing.neighborhood')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='post', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('neighborhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='listing.neighborhood')),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='listing.post')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='business',
            name='neighborHood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='business', to='listing.neighborhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL),
        ),
    ]
