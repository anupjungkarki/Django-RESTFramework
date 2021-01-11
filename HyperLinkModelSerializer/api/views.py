from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets

#   Use of ModelViewSet
class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
