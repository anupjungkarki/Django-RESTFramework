from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from .custom_auth import CustomAuthentication
from rest_framework.permissions import IsAuthenticated

#   Use of ModelViewSet
class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [CustomAuthentication]  # Custom Authentication
    permission_classes = [IsAuthenticated]  # Custom Permission Use
