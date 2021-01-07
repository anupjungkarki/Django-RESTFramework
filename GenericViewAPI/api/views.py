from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView ,RetrieveUpdateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView


class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetriveView(RetrieveAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeCreateView(CreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeUpdateView(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeDeleteView(DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# ListCreateAPIView
class EmployeeListCreateView(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


# RetriveDestroyAPIView
class EmployeeRetriveDestroyView(RetrieveDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class EmployeeRetriveUpdateView(RetrieveUpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetriveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
