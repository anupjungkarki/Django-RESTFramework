from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from .custom_throttling import CustomThrottle


#   Use of ModelViewSet
class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    authentication_classes = [SessionAuthentication]  # Custom Authentication
    permission_classes = [IsAuthenticatedOrReadOnly]  # Custom Permission Use
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    throttle_classes = [AnonRateThrottle, CustomThrottle]  # Use for custom throttle
