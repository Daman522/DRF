from django.db.models import fields
from rest_framework import serializers
from .models import *


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