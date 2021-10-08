from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=100)
    des=models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Car(models.Model):
    car_name = models.CharField(max_length=300)
    car_price = models.IntegerField()
    car_color = models.CharField(max_length=200)
    car_topspeed = models.FloatField(default=0)
    car_modelyear = models.IntegerField()
    car_milage = models.FloatField()


    def __str__(self):
        return f"NAME - {self.car_name} || COLOR - {self.car_color} || PRICE - {str(self.car_price)}"