from django.shortcuts import render
from pizza.models import PizzaInfo, Pizza, Ingredient
from rest_framework import serializers, viewsets
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt

class RelatedIngredient(serializers.RelatedField):
    def to_representation(self, value):
        return '%s' % (value.name)

class PizzaSerializer(serializers.ModelSerializer):
    pizza = RelatedIngredient(read_only=True)
    class Meta:
        model = Pizza
        fields='__all__'

class PizzaList(viewsets.ModelViewSet):
    queryset = Pizza.objects.all()
    serializer_class = PizzaSerializer


class IngerdientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields='__all__'

class IngerdientsList(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngerdientSerializer

class PizzaIngredientsSerializer(serializers.ModelSerializer):
    ingredient = RelatedIngredient(read_only=True)
    class Meta:
        model = Pizza
        fields=['ingredient']

class PizzaInfoSerializer(serializers.ModelSerializer):
    pizza_ingredients = PizzaIngredientsSerializer(many=True)
    class Meta:
        model = PizzaInfo
        fields=['id', 'name', 'cost', 'pizza_ingredients', 'image_url']

class PizzaInfoList(viewsets.ModelViewSet):
    queryset = PizzaInfo.objects.all()
    serializer_class = PizzaInfoSerializer
