# Generated by Django 4.1.7 on 2023-07-24 02:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0013_alter_audio_note_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio_note',
            name='audio',
        ),
        migrations.AddField(
            model_name='audio_note',
            name='audio_file',
            field=models.FileField(null=True, upload_to='media/audios/'),
        ),
        migrations.AddField(
            model_name='audio_note',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
