from django.urls import path
from .import views
from myapp.views import *

urlpatterns = [
    path('',views.apioverview, name='api-overview'),
    path('task-list/',views.taskList, name='task-list'),
    path('task-create/',views.taskCreate, name='task-create'),
    path('task-update/<int:pk>/',views.taskUpdate, name='task-update'),
    path('task-delete/<int:pk>/',views.taskDelete, name='task-delete'),
    path('car-view',CarList.as_view(), name='car-view'),
    path('car-detail/<int:pk>',CarDetail.as_view(), name='car-detail'),

]
