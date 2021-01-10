from rest_framework import serializers
from .models import Track, Singer


class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ['id', 'title', 'singer', 'album', 'duration']


class SingerSerializer(serializers.ModelSerializer):
    song = serializers.StringRelatedField(many=True, read_only=True)
    # song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='track-list')
    # song = serializers.SlugRelatedField(many=True, read_only=True, slug_field='album')
    # song = serializers.HyperlinkedIdentityField(view_name='track-list')

    class Meta:
        model = Singer
        fields = ['id', 'name', 'gender', 'song']
