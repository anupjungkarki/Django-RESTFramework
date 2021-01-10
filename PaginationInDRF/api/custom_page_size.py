from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination


#
# class CustomPagination(PageNumberPagination):
#     page_size = 5
#     page_query_param = 'page_size'
#     # page_size_query_param = 6
#     last_page_strings = 'end'


# For Limit OffsetPagination
# class LimitOffsetClass(LimitOffsetPagination):
#     default_limit = 5
#     limit_query_param = 'my_limit'

#  For CursorPagination Implementation
class CursorPaginationClass(CursorPagination):
    page_size = 3
    ordering = 'name'
    cursor_query_param = 'cu'
