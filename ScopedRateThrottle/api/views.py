
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.throttling import ScopedRateThrottle

# The ScopedRateThrottle class can be used to restrict access to specific parts of the API.
# This throttle will only be applied if the view that is being accessed includes a .throttle_scope property.
class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'list'

class EmployeeRetriveView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'retrive'

class EmployeeCreateView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'create'


class EmployeeUpdateView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'update'


class EmployeeDeleteView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    throttle_classes = [ScopedRateThrottle]
    throttle_scope = 'delete'

