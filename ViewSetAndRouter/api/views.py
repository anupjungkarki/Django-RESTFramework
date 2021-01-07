from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets


class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'New Data Created Successfully'})
        return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        id = pk
        if id is not None:
            employee = Employee.objects.get(id=id)
            serializer = EmployeeSerializer(employee)
            return Response(serializer.data)

    def update(self, request, pk=None):
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(instance=employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated Successfully'})
        return Response(serializer.errors)

    def partial_update(self, request, pk=None):
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(instance=employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated Successfully'})
        return Response(serializer.errors)

    def destroy(self, request, pk=None):
        employee = Employee.objects.get(id=pk)
        employee.delete()
        return Response({'msg': 'Data Deleted Successfully'})

