from django.contrib import admin

from app1.models import *

# Register your models here.
@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display = ('username', 'password', 'email', 'phone', 'type')

@admin.register(food_details)
class food_detailsAdmin(admin.ModelAdmin):
    list_display = ('food_name', 'serving_size', 'calories', 'protein', 'fat', 'carbs', 'type')

@admin.register(ingredient)
class ingredientAdmin(admin.ModelAdmin):
    list_display = ('food', 'ingredient_name', 'quantity', 'type_of_food')