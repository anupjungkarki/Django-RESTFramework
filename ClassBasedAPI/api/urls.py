from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.EmployeeGetPostView.as_view(), name='employee'),
    path('employee/<int:pk>', views.EmployeeGetPostView.as_view(), name='employee'),
    path('employee/create', views.EmployeeGetPostView.as_view(), name='create'),
    path('employee/update/<int:pk>', views.EmployeePutPatchView.as_view(), name='update'),
    path('employee/delete/<int:pk>', views.EmployeeDeleteView.as_view(), name='delete'),
]
