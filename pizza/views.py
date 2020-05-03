from django.shortcuts import render
from pizza.models import *
from rest_framework import serializers, viewsets
from rest_framework import status
from rest_framework.response import Response

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order

# ViewSets define the view behavior.
class OrderView(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

class PizzaInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PizzaInfo

class UserView(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, format=None):
        users = self.queryset
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PizzaInfoList(viewsets.ModelViewSet):
    queryset = PizzaInfo.objects.all()
    serializer_class = PizzaInfoSerializer

class IngerdientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient

class IngerdientsList(viewsets.ModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngerdientSerializer
