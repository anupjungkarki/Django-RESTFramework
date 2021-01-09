from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

#   Use of ModelViewSet
class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # If we want to use authentication and permission for particular class method only the use this
    # authentication_classes = [BasicAuthentication]  # Basic Authentication
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    permission_classes = [IsAdminUser]
