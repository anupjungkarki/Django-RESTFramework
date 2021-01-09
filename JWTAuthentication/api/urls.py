from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

# Creating Router Object
router = DefaultRouter()

# Registering EmployeeViewSet with Router
router.register('employee', views.EmployeeModelViewSet, basename='employee')
urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/', TokenObtainPairView.as_view(), name="token_obtain-pair"),
    path('refreshtoken/', TokenRefreshView.as_view(), name="token_refresh"),
    path('verifytoken/', TokenVerifyView.as_view(), name="token_verify"),
]

# Note To generate Token use this command
# http POST http://127.0.0.1:8000/api/gettoken/ username="superuser" password="superuser"

# OUTPUT will be:
# HTTP/1.1 200 OK
# Allow: POST, OPTIONS
# Content-Length: 438
# Content-Type: application/json
# Date: Sat, 09 Jan 2021 08:18:47 GMT
# Server: WSGIServer/0.2 CPython/3.8.3
# Vary: Accept
# X-Frame-Options: SAMEORIGIN
#
# {
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjEwMTgwNjI3LCJqdGkiOiI1NTQxYzEwZjFlNzA0MzM1OWMxYTY5MzI0MGIwMDkwNSIsInVzZXJfaWQiOjF9.I6BNeCLa
# ptcWyLCTdlHOnRfKUuGJea_unPZywuWdS5w",
#     "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxMDI2NjcyNywianRpIjoiZDhmMWQ1ZmEwYjI1NDU2ZGFlMTNmZGJjYWI2M2E4OTUiLCJ1c2VyX2lkIjoxfQ.nOMMm
# xllW_EOr5gdGBgw6gkzrdMAq1PhP7nEKwjaCLo"
# }

# Note To Verify Token use this command
# http POST http://127.0.0.1:8000/api/verifytoken/ token="access_token"

# Note To Use Refresh Token use this command
# http POST http://127.0.0.1:8000/api/refreshtoken/ token="refresh_token"


# To access API
# http http://127.0.0.1:8000/api/employee/ "Authorization:Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI
# 1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjEwMTkyMDI2LCJqdGkiOiJjZTYzZDc4NmNjYjk0MTc2YmMyNWQ1ZmIxZTU3ZTIxYyIsInVzZXJfaWQiOjJ9.a3wMBIKJiXQhYPRmjUxCZST63kPllDsvjY3NUujptLU"

# To POST Data
# http -f POST http://127.0.0.1:8000/api/employee/ id=3 email=karki@gmail.com mobile_no=9836362562 name=Karki reg_no=36236535253573 "Authorization:Bearer Token_axxess_name_here

# To PUT Data
# http -f PUT http://127.0.0.1:8000/api/employee/3 id=3 email=karki@gmail.com name=Karki "Authorization:Bearer Token_access_name_here

# To DELETE Data
# http -f DELETE http://127.0.0.1:8000/api/employee/3 "Authorization:Bearer Token_access_name_here
