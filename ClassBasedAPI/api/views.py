from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.views import APIView


class EmployeeGetPostView(APIView):
    def get(self, request, pk=None, format=None):
        if pk is not None:
            employee = Employee.objects.get(id=pk)
            serializer = EmployeeSerializer(employee, many=False)
            return Response(serializer.data)

        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'New Data Created Successfully'})
        return Response(serializer.errors)


class EmployeePutPatchView(APIView):
    def put(self, request, pk, format=None):
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(instance=employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Data Updated Successfully'})
        return Response(serializer.errors)

    def patch(self, request, pk, format=None):
        employee = Employee.objects.get(id=pk)
        serializer = EmployeeSerializer(instance=employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Partial Data Updated Successfully'})
        return Response(serializer.errors)


class EmployeeDeleteView(APIView):
    def delete(self, request, pk, format=None):
        employee = Employee.objects.get(id=pk)
        employee.delete()
        return Response({'msg': 'Data Deleted Successfully'})
