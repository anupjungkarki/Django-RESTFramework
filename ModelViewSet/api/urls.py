from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Creating Router Object
router = DefaultRouter()

# Registering EmployeeViewSet with Router
router.register('employee', views.EmployeeModelViewSet, basename='employee')
router.register('employees', views.EmployeeReadOnlyModelViewSet, basename='employees')
urlpatterns = [
    path('', include(router.urls))
]
