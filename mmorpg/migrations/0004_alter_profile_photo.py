# Generated by Django 4.2.1 on 2023-05-06 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmorpg', '0003_remove_profile_contact_info_profile_discord_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/profile_photos'),
        ),
    ]
