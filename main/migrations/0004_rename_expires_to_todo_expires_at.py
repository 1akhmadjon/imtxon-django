# Generated by Django 4.2.5 on 2023-10-30 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_rename_todo_text_todo_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='expires_to',
            new_name='expires_at',
        ),
    ]
