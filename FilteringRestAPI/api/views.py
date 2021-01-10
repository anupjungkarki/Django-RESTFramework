from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.generics import ListAPIView
from django_filters import rest_framework as filters
from rest_framework.filters import SearchFilter, OrderingFilter


class EmployeeListView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    # Overwriting the get_queryset to filter according to login user
    # def get_queryset(self):
    #     user = self.request.user
    #     return Employee.objects.filter(manager=user)

    # Filtering API using FilterBackend Module
    # filter_backends = (filters.DjangoFilterBackend,)
    # filterset_fields = ['name', 'manager', ]

    # Another Method to Search Using Search Filter
    filter_backends = [SearchFilter]
    # To search using single field
    search_fields = ['manager']
    # To search either by name or manager
    # search_fields = ['name', 'manager']
    # Search according to single character
    # search_fields = ['^name']

    # For Ordering The API  Data
    # filter_backends = [OrderingFilter]
    # We can also give the Ordering_Fields For Ordering According To Fields
    # ordering_fields = ['name']
