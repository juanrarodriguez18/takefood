# encoding=utf8
# Copyright 2018 by TakeAdvantageOfFood contributors. All rights reserved.
#
# This file is part of TakeAdvantageOfFood.
#
#     TakeAdvantageOfFood is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     TakeAdvantageOfFood is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with TakeAdvantageOfFood.  If not, see <http:#www.gnu.org/licenses/>.
from django.core.management.base import BaseCommand
from django.db import transaction
from application.models import Recipe, Ingredient
import csv

class Command(BaseCommand):
    def leer_fichero_csv(self, file):
        f = open(file, "r", encoding="utf8")
        s = csv.reader(f)
        return [s, f]

    def populateDatabase(self):
        self.populateRecipes()
        self.populateIngredients()

    """
    recipe_id = models.IntegerField()
    name = models.CharField(max_length=100)
    ease_of_prep = models.CharField(max_length=100)
    recipe_type = models.CharField(max_length=100)
    prep_time = models.IntegerField(default=0)
    photo = models.URLField()
    ingredients_quantity = models.IntegerField()
    link = models.URLField()
    """
    @transaction.atomic
    def populateRecipes(self):
        print("Populating Recipes")
        i = 0
        fichero_csv = self.leer_fichero_csv("csv/Recipes.csv")
        recipes = fichero_csv[0]
        prep_time = 0
        ingredients_quantity = 0

        Recipe.objects.all().delete()
        for recipe in recipes:
            if i != 0:
                if recipe[4]:
                    prep_time = recipe[4]

                if recipe[6]:
                    ingredients_quantity = recipe[6]
                Recipe.objects.get_or_create(recipe_id= recipe[0], name= recipe[1], ease_of_prep= recipe[2], recipe_type= recipe[3],
                                             prep_time= prep_time, photo= recipe[5], ingredients_quantity= ingredients_quantity, link= recipe[7])
            i += 1

        fichero_csv[1].close()

    """
    ingredient_name = models.CharField(max_length=100)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True, null=True)
    """
    @transaction.atomic
    def populateIngredients(self):
        print("Populating Ingredients")
        i = 0
        fichero_csv = self.leer_fichero_csv("csv/Ingredients.csv")
        ingredients = fichero_csv[0]

        Ingredient.objects.all().delete()
        for ingredient in ingredients:
            if i != 0:
                Ingredient.objects.get_or_create(ingredient_name= ingredient[1], recipe = Recipe.objects.get(recipe_id= ingredient[0]))
            i += 1

        fichero_csv[1].close()

    def handle(self, *args, **options):
        self.populateDatabase()