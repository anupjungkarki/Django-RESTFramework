from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Registering EmployeeViewSet with Router
router.register('employee', views.EmployeeModelViewSet, basename='employee')
urlpatterns = [
    path('', include(router.urls)),
    # It will use in session Authentication for login Interface Show Routes
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
