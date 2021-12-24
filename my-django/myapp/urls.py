from django.urls import path
from .import views
from myapp.views import *
from knox import views as knox_views

urlpatterns = [
    path('',views.apioverview, name='api-overview'),
    # path('task-list/',views.taskList, name='task-list'),
    # path('task-create/',views.taskCreate, name='task-create'),
    # path('task-update/<int:pk>/',views.taskUpdate, name='task-update'),
    # path('task-delete/<int:pk>/',views.taskDelete, name='task-delete'),
    # path('car-view',CarList.as_view(), name='car-view'),
    # path('car-detail/<int:pk>',CarDetail.as_view(), name='car-detail'),
    path('api/register/', RegisterAPI.as_view(), name='register'),
    # path('api/login/', LoginAPI.as_view(), name='login'),
    # path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    # path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),

]
