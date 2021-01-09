from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly, \
    DjangoModelPermissions, DjangoModelPermissionsOrAnonReadOnly, DjangoObjectPermissions


#   Use of ModelViewSet
class EmployeeModelViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # If we want to use authentication and permission for particular class method only then use this
    authentication_classes = [SessionAuthentication]  # Session Authentication
    # permission_classes = [IsAuthenticated]
    # permission_classes = [AllowAny]
    # permission_classes = [IsAdminUser]
    # permission_classes = [
    #     IsAuthenticatedOrReadOnly]  # It is used for Unauthenticated user to view data but not make operation
    # But if user is LoggedIn that is authenticated he can get permission for any operations
    # permission_classes = [DjangoModelPermissions]  # It is use for Model Based Permission To give access to the user
    # in the particular api from the model permission section according to that user can get role for those access
    # in the api
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]  # It will use similar to DjangoModelPermissions for
    # Authenticate user but UnAuthenticated user can Readonly the API View
    permission_classes = [DjangoObjectPermissions]
