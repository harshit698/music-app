# Generated by Django 2.0.1 on 2018-01-31 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='song_tiitle',
            new_name='song_title',
        ),
    ]