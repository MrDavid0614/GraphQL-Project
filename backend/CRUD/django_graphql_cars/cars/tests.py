from django.test import RequestFactory,TestCase
from .models import Car
from graphene.test import Client
from django_graphql_cars.cars.schema import schema
from django.contrib.auth.models import AnonymousUser
import requests

class TestCarModel(TestCase):

    def createCar(self, brand, model, color, year):
        car = Car.objects.create(
            brand=brand, 
            model=model, 
            color=color, 
            year=year)

        return car

    def setUp(self):
        Car.objects.all().delete()
    
    def test_create_car_successfully(self):
        Car.objects.all().delete()
        car1 = self.createCar("Kia", "Pikanto", "White", "2018-05-15")
        
        self.assertEqual(Car.objects.get(brand="Kia"), car1)
    
    def test_car_is_in_database(self):
        Car.objects.all().delete()
        car1 = self.createCar("Kia", "Pikanto", "White", "2018-05-15")

        self.assertIn(car1, Car.objects.all())

    def test_car_is_not_in_database(self):
        Car.objects.all().delete()
        car1 = Car()

        self.assertNotIn(car1, Car.objects.all())
    
    def test_car_is_not_none(self):
        Car.objects.all().delete()
        car1 = Car()

        self.assertIsNotNone(car1)

    def test_car_is_none(self):
        Car.objects.all().delete()
        car1 = None

        self.assertIsNone(car1) 

    def test_all_objects_in_cars_are_cars(self):
        Car.objects.all().delete()
        for car in Car.objects.all():
            self.assertIsInstance(car, Car)

# class TestGraphQL(TestCase):

#     def test_get_all_cars(self):
#         req = RequestFactory().get('graphql/')
#         req.user = AnonymousUser()
#         client = Client(schema)
#         client.user = AnonymousUser()
#         executed = client.execute(
#             '''
#             query {
#                 cars {
#                     brand
#                     model
#                     color
#                     year
#                 }
#             }
#             ''', context_value=req)
#         response = requests.post('http://127.0.0.1:8000/graphql/', json={'query': '''
#                                             query {
#                                                 cars {
#                                                     brand
#                                                     model
#                                                     color
#                                                     year
#                                                 }
#                                             }
#                                         '''})
#         self.assertEqual(executed, response.json())