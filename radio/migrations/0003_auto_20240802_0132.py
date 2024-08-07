# Generated by Django 3.2.25 on 2024-08-01 22:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('radio', '0002_usersongactivity'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usersongactivity',
            old_name='last_updated',
            new_name='timestamp',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='usersongactivity',
            name='current_song',
        ),
        migrations.AddField(
            model_name='usersongactivity',
            name='is_playing',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usersongactivity',
            name='song',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='radio.song'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='song',
            name='uploaded_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='usersongactivity',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('members', models.ManyToManyField(related_name='custom_groups', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='usersongactivity',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='radio.group'),
        ),
    ]
