# Generated by Django 5.1.7 on 2025-03-24 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_alter_book_subtitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.TextField(default='text'),
            preserve_default=False,
        ),
    ]
