from django.test import TestCase
from .models import Car

class TestCarModel(TestCase):

    def test_create_car_model_succesful(TestCase):
        car1 = Car.objects.create(
            brand="Toyota", 
            model="Camry", 
            color="Red", 
            year="2018-02-06")
        
        assert Car.objects.all(), car1