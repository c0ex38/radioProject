from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='custom_groups')

    def __str__(self):
        return self.name


class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='songs/')
    uploaded_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)  # Bu satırı ekleyin

    def __str__(self):
        return self.title

class Comment(models.Model):
    song = models.ForeignKey(Song, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.user.username} - {self.song.title}'


class UserSongActivity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=True)
    is_playing = models.BooleanField(default=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.user.username} - {self.song.title} - {self.is_playing}'

    @property
    def current_song(self):
        return self.song.title

    @property
    def last_updated(self):
        return self.timestamp


class Announcement(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='announcements/')

    def __str__(self):
        return self.title
