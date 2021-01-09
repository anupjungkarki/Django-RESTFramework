from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .auth import CustomAuthToken

# Creating Router Object
router = DefaultRouter()

# Registering EmployeeViewSet with Router
router.register('employee', views.EmployeeModelViewSet, basename='employee')
urlpatterns = [
    path('', include(router.urls)),
    # It will use in session Authentication Routes for to Show  login Interface
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    # for authtoken
    # path('gettoken/', obtain_auth_token),
    path('gettoken/', CustomAuthToken.as_view())
]
