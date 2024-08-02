from django.contrib import admin
from .models import Song, Comment, UserSongActivity, Group, Announcement

from django.contrib import admin
from django.utils.translation import gettext_lazy as _


class UserSongActivityAdmin(admin.ModelAdmin):
    list_display = ('user', 'song', 'is_playing', 'timestamp')


admin.site.site_header = _("DGN Radyo Admin")
admin.site.site_title = _("Django Yönetimi Başlığı")
admin.site.index_title = _("Yönetim Paneline Hoşgeldiniz")

admin.site.register(Song)
admin.site.register(Comment)
admin.site.register(UserSongActivity, UserSongActivityAdmin)
admin.site.register(Group)
admin.site.register(Announcement)
