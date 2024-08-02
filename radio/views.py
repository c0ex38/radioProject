import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt

from .forms import UserCreationForm
from .models import Song, UserSongActivity, Announcement


@login_required
@csrf_exempt
def update_current_song(request, song_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        current_time = data.get('current_time', 0)
        duration = data.get('duration') or 0  # Use 0 if duration is not provided
        song = Song.objects.get(id=song_id)
        activity, created = UserSongActivity.objects.update_or_create(
            user=request.user,
            defaults={'song': song, 'current_time': current_time, 'duration': duration, 'is_playing': True}
        )
        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'fail'}, status=400)

@login_required
def song_list(request):
    songs = Song.objects.all()
    announcements = Announcement.objects.all()
    return render(request, 'radio/song_list.html', {'songs': songs, 'announcements': announcements})

@login_required
def play_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    UserSongActivity.objects.update_or_create(user=request.user, defaults={'song': song, 'is_playing': True})
    return redirect('song_list')


@login_required
def stop_song(request):
    UserSongActivity.objects.filter(user=request.user).update(is_playing=False)
    return redirect('song_list')


@login_required
def update_current_song(request, song_id):
    song = get_object_or_404(Song, id=song_id)
    group = request.user.groups.first()
    if group:
        UserSongActivity.objects.filter(group=group).update(song=song, is_playing=True)
    else:
        UserSongActivity.objects.update_or_create(user=request.user, defaults={'song': song, 'is_playing': True})
    return JsonResponse({'status': 'success'})


def get_current_song(request):
    if request.user.is_authenticated:
        group = request.user.groups.first()
        if group:
            current_song = UserSongActivity.objects.filter(group=group, is_playing=True).first()
        else:
            current_song = UserSongActivity.objects.filter(user=request.user, is_playing=True).first()
        if current_song:
            return JsonResponse({
                'song_id': current_song.song.id,
                'song_title': current_song.song.title,
                'song_artist': current_song.song.artist,
                'song_url': current_song.song.audio_file.url
            })
    return JsonResponse({'song_id': None})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('song_list')
        else:
            return render(request, 'radio/login.html', {'error': 'Invalid username or password'})
    return render(request, 'radio/login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('song_list')
    else:
        form = UserCreationForm()
    return render(request, 'radio/register.html', {'form': form})
