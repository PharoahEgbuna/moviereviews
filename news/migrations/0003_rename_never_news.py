# Generated by Django 5.1.4 on 2025-01-07 15:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_rename_news_never'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Never',
            new_name='News',
        ),
    ]
