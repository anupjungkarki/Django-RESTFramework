from django.urls import path
from . import views

urlpatterns = [
    path('employee/', views.EmployeeListView.as_view(), name='employee'),
    path('employee/<int:pk>', views.EmployeeRetriveView.as_view(), name='employee'),
    path('employee/create', views.EmployeeCreateView.as_view(), name='create'),
    path('employee/update/<int:pk>', views.EmployeeUpdateView.as_view(), name='update'),
    path('employee/delete/<int:pk>', views.EmployeeDeleteView.as_view(), name='delete'),
    path('employee/listcreate', views.EmployeeListCreateView.as_view(), name='listcreate'),
    path('employee/retrivedestroy/<int:pk>', views.EmployeeRetriveDestroyView.as_view(), name='retrivedestroy'),
    path('employee/retriveupdate/<int:pk>', views.EmployeeRetriveUpdateView.as_view(), name='retrivedestroy'),
    path('employee/retriveupdatedestroy/<int:pk>', views.EmployeeRetriveUpdateDestroyView.as_view(), name='retrivedestroy'),

]
