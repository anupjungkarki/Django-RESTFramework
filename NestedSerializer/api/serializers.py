from rest_framework import serializers
from .models import Track, Singer


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'title', 'singer', 'album', 'duration']


class SingerSerializer(serializers.ModelSerializer):
    song = TrackSerializer(many=True, read_only=True)

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']
