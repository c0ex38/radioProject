# Generated by Django 3.2.25 on 2024-08-02 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('radio', '0003_auto_20240802_0132'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('audio_file', models.FileField(upload_to='announcements/')),
            ],
        ),
    ]
