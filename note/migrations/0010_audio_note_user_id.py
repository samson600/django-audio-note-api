# Generated by Django 4.1.7 on 2023-06-27 18:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0009_remove_audio_note_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio_note',
            name='user_id',
            field=models.ForeignKey(default=5, on_delete=django.db.models.deletion.CASCADE, to='note.users'),
            preserve_default=False,
        ),
    ]
