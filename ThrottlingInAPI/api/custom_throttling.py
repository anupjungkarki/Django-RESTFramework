# This for giving throttling access for different api class at different TimeStamp
from rest_framework.throttling import UserRateThrottle

class CustomThrottle(UserRateThrottle):
    scope = 'custom'
