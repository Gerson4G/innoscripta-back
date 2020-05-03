from django.shortcuts import render
from pizza.models import User
from rest_framework import serializers, viewsets
from rest_framework import status
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.decorators import api_view

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=200)


class UserView(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = ()

    @classmethod
    def get_extra_actions(cls):
        return []

    def get(self, request, format=None):
        users = self.queryset
        serializer = self.serializer_class(users, many=True)
        return Response(serializer.data)

    @csrf_exempt
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):

    serializer_class = LoginSerializer
    def perform_create(self, serializer):
        pass
    
    def post(self, request):
        from django.core.exceptions import ObjectDoesNotExist
        email = request.data["email"]
        password = request.data["password"]
        try:
            user = User.objects.get(email=email)
            if user.password == password:
                serializer = self.serializer_class(data=user.__dict__)
                if serializer.is_valid():
                    return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response("Wrong password", status=status.HTTP_401_UNAUTHORIZED)
        except ObjectDoesNotExist:
            return Response("Email not found", status=status.HTTP_404_NOT_FOUND)
            