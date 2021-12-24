from django.db.models import fields
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=('id','username','email','password')
        extra_kwargs={'password':{'write_only':True}}

    def create(self,validate_data):
        user=User.objects.create_user(validate_data['username'],validate_data['email'],validate_data['password'])
        return user



class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"
        


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        if data['car_modelyear'] > 2021:
            raise serializers.ValidationError("ERROR")
        return data