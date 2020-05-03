"""innoscripta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from rest_framework import routers
from pizza.views.ingredients import *
from pizza.views.user import UserView, LoginView
from pizza.views.order import OrderView
from django.views.decorators.csrf import csrf_exempt

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'orders', OrderView)
router.register(r'users', UserView, basename='Users')
router.register(r'pizza-info', PizzaInfoList)
router.register(r'pizza', PizzaList, basename="Pizza")
router.register(r'ingredients', IngerdientsList)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/users/login/', LoginView.as_view()),
]
