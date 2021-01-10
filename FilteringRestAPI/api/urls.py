from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.EmployeeListView.as_view(), name='employee'),
]
