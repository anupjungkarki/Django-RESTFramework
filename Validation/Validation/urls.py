from django.contrib import admin
from django.urls import path
from ValidationREST import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis_create/', views.student_create, name='apis_create'),
]
