from django.shortcuts import render
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
@api_view(['GET'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def employee_api(request, pk=None):
    if request.method == "GET":
        if pk is not None:
            employee = Employee.objects.get(id=pk)
            serializer = EmployeeSerializer(employee, many=False)
            return Response(serializer.data)

        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def employee_create(request):
    if request.method == "POST":
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'New Data Created Successfully'})
        return Response(serializer.errors)


@api_view(['PUT', 'PATCH'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def employee_update(request, pk):
    if request.method == 'PUT':
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(instance=employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated Successfully'})
        return Response(serializer.errors)

    if request.method == 'PATCH':
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(instance=employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated Successfully'})
        return Response(serializer.errors)


@api_view(['DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def employee_delete(request, pk):
    if request.method == 'DELETE':
        employee = Employee.objects.get(id=pk)
        employee.delete()
        return Response({'msg': 'Data Deleted Successfully'})

