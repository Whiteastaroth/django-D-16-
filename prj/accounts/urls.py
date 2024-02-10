from django.urls import path
from .views import SignUp, GetCode

urlpatterns = [
    path('signup', SignUp.as_view(), name='signup'),
    path('code/<str:user>', GetCode.as_view(), name='code'),
]
