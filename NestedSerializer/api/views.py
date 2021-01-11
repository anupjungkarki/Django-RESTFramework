from django.shortcuts import render
from .serializers import SingerSerializer, TrackSerializer
from rest_framework import viewsets
from .models import Track, Singer


# Create your views here.

class SingerViewSet(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class TrackViewSet(viewsets.ModelViewSet):
    queryset = Track.objects.all()
    serializer_class = TrackSerializer
