from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Registering EmployeeViewSet with Router
router.register('singer', views.SingerViewSet, basename='singer')
router.register('track', views.TrackViewSet, basename='track')
urlpatterns = [
    path('', include(router.urls))
]
