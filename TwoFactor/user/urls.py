from django.urls import path
from .import views
from user.views import *
from codes.views import *


urlpatterns = [
    path('',views.home_view, name='home-view'),
    path('login/',views.auth_view, name='login-view'),
    path('verify',views.verify_view, name='verify-view'),


]
