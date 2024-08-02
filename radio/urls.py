from django.urls import path
from . import views

urlpatterns = [
    path('', views.song_list, name='song_list'),
    path('play/<int:song_id>/', views.play_song, name='play_song'),
    path('stop/', views.stop_song, name='stop_song'),
    path('update_current_song/<int:song_id>/', views.update_current_song, name='update_current_song'),
    path('get_current_song/', views.get_current_song, name='get_current_song'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.register, name='register'),
]
