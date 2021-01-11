from django.contrib import admin
from .models import Singer, Track


# Register your models here.
@admin.register(Singer)
class SingerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'gender']


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'singer', 'album', 'duration']
