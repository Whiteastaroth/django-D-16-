from django.urls import path
from .views import SignUp, GetCode
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('code/<str:user>', GetCode.as_view(), name='code'),
]
