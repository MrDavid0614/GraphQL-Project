from django.test import TestCase
from .models import Car

class TestCarModel(TestCase):

    def test_create_car_succesful(self):
        car1 = Car.objects.create(
            brand="Kia", 
            model="Pikanto", 
            color="White", 
            year="2018-02-06")
        
        self.assertEqual(Car.objects.get(brand="Kia"), car1)
    