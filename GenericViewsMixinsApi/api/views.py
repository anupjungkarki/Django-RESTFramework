# Generic API Views and Model Mixing
from .serializers import EmployeeSerializer
from .models import Employee
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin


class EmployeeList(GenericAPIView, ListModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class EmployeeCreate(GenericAPIView, CreateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class EmployeeRetrive(GenericAPIView, RetrieveModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class EmployeeUpdate(GenericAPIView, UpdateModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class EmployeeDelete(GenericAPIView, DestroyModelMixin):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
