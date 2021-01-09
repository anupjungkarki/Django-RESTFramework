from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .custom_permissions import MyPermission


#   Use of ModelViewSet
class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication]  # Session Authentication
    permission_classes = [MyPermission]  # Custom Permission Use
