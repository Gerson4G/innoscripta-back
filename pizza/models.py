from django.db import models

class User(models.Model):
    email=models.EmailField(max_length=200, unique=True)
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=512)
    password=models.CharField(max_length=512)
    
class PizzaInfo(models.Model):
    name=models.CharField(max_length=200)

class Ingredient(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)

class Order(models.Model):
    order_number=models.IntegerField()
    pizza=models.ForeignKey(to=PizzaInfo, on_delete=models.CASCADE)
    user=models.ForeignKey(to=User, on_delete=models.CASCADE)
    date=models.DateField()
    cost=models.FloatField()
    quantity=models.IntegerField()


class Pizza(models.Model):
    pizza=models.ForeignKey(to=PizzaInfo, on_delete=models.CASCADE)
    ingredient=models.ForeignKey(to=Ingredient, on_delete=models.CASCADE)
    