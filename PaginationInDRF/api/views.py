from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
# from .custom_page_size import CustomPagination
# from .custom_page_size import LimitOffsetClass
from .custom_page_size import CursorPaginationClass


# class EmployeeListView(ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     # pagination_class = PageNumberPagination
#     # For custom Pagination
#     pagination_class = CustomPagination


# For Limit Offset Pagination
# class EmployeeListView(ListAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     pagination_class = LimitOffsetClass

# For CursorPagination Pagination
class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CursorPaginationClass
