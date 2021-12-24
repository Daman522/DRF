from django.urls import path
from .import views
# from user.views import *
from codes.views import *


urlpatterns = [
    path('',views.home, name='home'),
  

]
