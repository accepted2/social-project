# Generated by Django 5.1.2 on 2024-11-21 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_photo_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='socialproject\\media\\images\\default_item_logo.jpg', upload_to='users/%Y/%m/%d'),
        ),
    ]