"""django_graphql_cars URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django_graphql_cars.schema import schema
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, sys, logging

logger = logging.getLogger(__name__)

def create_car(request):
    body = json.loads(request.body.decode('utf-8'))
    result = schema.execute(body['query'])
    response = {}
    response['data'] = result.data
    return JsonResponse(response)

def get_cars(request):
    result = schema.execute(
        '''
        query getCars {

            cars {
                id
                brand
                model
                color
                year
            }

        }
        '''
    )
    response = {}
    response['data'] = result.data
    return JsonResponse(response)

def update_car(request):
    body = json.loads(request.body.decode('utf-8'))
    result = schema.execute(body['query'])
    logger.info(json.dumps(body['query'], indent=4))
    response = {}
    response['query'] = result.data
    return JsonResponse(response)

def delete_car(request):
    body = json.loads(request.body.decode('utf-8'))
    result = schema.execute(body['query'])
    response = {}
    response['query'] = result.data
    return JsonResponse(response)

urlpatterns = [
    path('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    path('createCar/', csrf_exempt(create_car)),
    path('getCars/', csrf_exempt(get_cars)),
    path('updateCar/', csrf_exempt(update_car)),
    path('deleteCar/', csrf_exempt(delete_car))
]
