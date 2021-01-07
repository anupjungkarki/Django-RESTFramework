from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.EmployeeList.as_view(), name='employee'),
    path('employee/<int:pk>', views.EmployeeRetrive.as_view(), name='employee'),
    path('employee/create', views.EmployeeCreate.as_view(), name='create'),
    path('employee/update/<int:pk>', views.EmployeeUpdate.as_view(), name='update'),
    path('employee/delete/<int:pk>', views.EmployeeDelete.as_view(), name='delete'),
]
