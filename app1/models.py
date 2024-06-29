from django.db import models


# Create your models here.
class user(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField(unique=True)


class food_details(models.Model):
    food_name = models.CharField(max_length=30)
    serving_size = models.DecimalField(max_digits=5, decimal_places=2)
    calories = models.DecimalField(max_digits=5, decimal_places=2)
    protein = models.DecimalField(max_digits=5, decimal_places=2)
    fat = models.DecimalField(max_digits=5, decimal_places=2)
    carbs = models.DecimalField(max_digits=5, decimal_places=2)
    type = models.CharField(max_length=30)


class ingredient(models.Model):
    food = models.ForeignKey(food_details, on_delete=models.CASCADE)
    ingredient_name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    type_of_food = models.CharField(max_length=30)
