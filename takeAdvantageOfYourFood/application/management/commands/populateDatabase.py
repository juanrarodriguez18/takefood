# encoding=utf8

from django.core.management.base import BaseCommand
from django.db import transaction
from application.models import Recipe, Ingredient
from django.db.models import Count

class Command(BaseCommand):
    def leer_fichero(self, file):
        f = open(file, "r", encoding="utf8")
        s = f.read()
        f.close()
        return s

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
        recipes = self.leer_fichero("csv/Recipes.csv").splitlines()
        prep_time = 0
        ingredients_quantity = 0

        Recipe.objects.all().delete()
        for recipe in recipes:
            if i != 0:
                #TODO PARSE XML
                info_recipe = recipe.split(",")
                
                if info_recipe[4]:
                    prep_time = info_recipe[4]

                if info_recipe[6]:
                    ingredients_quantity = info_recipe[6]
                print(len(info_recipe))
                print(info_recipe)
                Recipe.objects.get_or_create(recipe_id= info_recipe[0], name= info_recipe[1], ease_of_prep= info_recipe[2], recipe_type= info_recipe[3],
                                             prep_time= prep_time, photo= info_recipe[5], ingredients_quantity= ingredients_quantity, link= info_recipe[7])
            i += 1

    @transaction.atomic
    def populateIngredients(self):
        print("Populating Ingredients")
        ingredients = self.leer_fichero("csv/Ingredients.csv").splitlines()
        #Director.objects.all().delete()

    def handle(self, *args, **options):
        self.populateDatabase()