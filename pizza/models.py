from django.db import models

class User(models.Model):
    email=models.EmailField(max_length=200, unique=True)
    phone=models.CharField(max_length=200)
    address=models.CharField(max_length=512)
    password=models.CharField(max_length=512)
    name=models.CharField(max_length=512, default="")

    def __str__(self):
        return '{} - {}'.format(self.name, self.email)

class PizzaInfo(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return '{}'.format(self.name)

class Ingredient(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.name)

class Order(models.Model):
    order_number=models.IntegerField()
    pizza=models.ForeignKey(to=PizzaInfo, on_delete=models.CASCADE)
    user=models.ForeignKey(to=User, on_delete=models.CASCADE)
    date=models.DateField()
    cost=models.FloatField()
    quantity=models.IntegerField()

    def __str__(self):
        return 'Order #: {} - A {} pizza - By {}'.format(self.order_number, self.pizza.name, self.user.name)

class Pizza(models.Model):
    pizza=models.ForeignKey(to=PizzaInfo, on_delete=models.CASCADE, related_name='pizza_ingredients')
    ingredient=models.ForeignKey(to=Ingredient, on_delete=models.CASCADE, related_name='ingredients')
    
    