# Generated by Django 5.1.3 on 2024-12-08 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, upload_to='book_covers/'),
        ),
    ]
