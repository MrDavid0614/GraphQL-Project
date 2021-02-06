import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from django_graphql_cars.cars.models import Car

class CarType(DjangoObjectType):
    class Meta:
        model = Car

class CarInput(graphene.InputObjectType):
    id= graphene.Int()
    brand = graphene.String()
    model = graphene.String()
    color = graphene.String()
    year = graphene.Date()

class CreateCar(graphene.Mutation):
    class Arguments:
        input = CarInput(required=True)

    ok = graphene.Boolean()
    car = graphene.Field(CarType)

    @staticmethod
    def mutate(root, info, input=None):
        ok = True
        car_instance = Car(brand=input.brand, model=input.model, color=input.color, year=input.year)
        car_instance.save()
        return CreateCar(ok=ok, car=car_instance)

class UpdateCar(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
        input = CarInput(required=True)

    ok = graphene.Boolean()
    car = graphene.Field(CarType)

    @staticmethod
    def mutate(root, info, id, input=None):
        ok = False
        car_instance = Car.objects.get(pk=id)
        if car_instance:
            ok = True
            car_instance.brand = input.brand
            car_instance.model = input.model
            car_instance.color = input.color
            car_instance.year = input.year
            car_instance.save()
            return UpdateCar(ok=ok, car=car_instance)
        return UpdateCar(ok=ok, car=None)

class DeleteCar(graphene.Mutation):
    class Arguments:
        id = graphene.Int(required=True)
    
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, id):
        ok = False
        car_instance = Car.objects.get(pk=id)
        if car_instance:
            ok = True
            car_instance.delete()
            return DeleteCar(ok=ok)
        return DeleteCar(ok=ok)

class DeleteAllCars(graphene.Mutation):
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info):
        ok = False
        cars = Car.objects.all()
        if cars:
            ok = True
            cars.delete()
            return DeleteAllCars(ok=ok)
        return DeleteAllCars(ok=ok)

class Query(ObjectType):
    car = graphene.Field(CarType, id=graphene.Int())
    cars = graphene.List(CarType)

    def resolve_car(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Car.objects.get(pk=id)
    
    def resolve_cars(self, info, **kwargs):
        return Car.objects.all()

class Mutation(graphene.ObjectType):
    create_car = CreateCar.Field()
    update_car = UpdateCar.Field()
    delete_car = DeleteCar.Field()
    delete_all_cars = DeleteAllCars.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)