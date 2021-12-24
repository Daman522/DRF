from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework import permissions
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from rest_framework import generics, permissions

# # Create your views here.
 

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

# # class LoginAPI(KnoxLoginView):
# #     permission_classes = (permissions.AllowAny,)

# #     def post(self, request, format=None):
# #         serializer = AuthTokenSerializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         user = serializer.validated_data['user']
# #         login(request, user)
# #         return super(LoginAPI, self).post(request, format=None)

# # class UserAPI(generics.RetrieveAPIView):
# #     permission_classes = [permissions.IsAuthenticated,]
# #     serializer_class = UserSerializer

# #     def get_object(self):
# #         return self.request.user



@api_view(['GET'])
def apioverview(request):
    api_urls={
        'List':'/task-list/',
        'Create':'/task-create/',
    }
    return Response(api_urls)


# @api_view(['GET'])
# def taskList(request):
#     tasks=Task.objects.all()
#     serializer=TaskSerializer(tasks,many=True)
#     return Response(serializer.data)


# @api_view(['POST'])
# def taskCreate(request):
    
#     serializer=TaskSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)

# @api_view(['POST'])
# def taskUpdate(request,pk):
#     task=Task.objects.get(id=pk)
#     serializer=TaskSerializer(instance=task,data=request.data)
#     if serializer.is_valid():
#         serializer.save()

#     return Response(serializer.data)


# @api_view(['DELETE'])
# def taskDelete(request,pk):
#     task=Task.objects.get(id=pk)
#     task.delete()
#     return Response('deleted')


# class CarList(generics.ListCreateAPIView):
#     serializer_class=CarSerializer
#     queryset=Car.objects.all()


# class CarDetail(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class=CarSerializer
#     queryset=Car



# # class RegisterAPI(generics.GenericAPIView):
# #     serializer_class = RegisterSerializer

# #     def post(self, request, *args, **kwargs):
# #         serializer = self.get_serializer(data=request.data)
# #         serializer.is_valid(raise_exception=True)
# #         user = serializer.save()
# #         return Response({
# #         "user": UserSerializer(user, context=self.get_serializer_context()).data,
# #         "token": AuthToken.objects.create(user)[1]
# #         })