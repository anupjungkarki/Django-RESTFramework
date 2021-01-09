from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.employee_api, name='employee'),
    path('employee/<int:pk>', views.employee_api, name='employee'),
    path('employee/create', views.employee_create, name='create'),
    path('employee/update/<int:pk>', views.employee_update, name='update'),
    path('employee/delete/<int:pk>', views.employee_delete, name='delete'),
]
