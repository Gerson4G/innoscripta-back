from django.shortcuts import render
from pizza.models import *
from rest_framework import serializers, viewsets
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields='__all__'

# ViewSets define the view behavior.
class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class PizzaInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaInfo
        fields='__all__'

class PizzaInfoList(viewsets.ModelViewSet):
    queryset = PizzaInfo.objects.all()
    serializer_class = PizzaInfoSerializer

class IngerdientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields='__all__'

class IngerdientsList(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngerdientSerializer
