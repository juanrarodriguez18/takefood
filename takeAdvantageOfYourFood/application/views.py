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
import os

from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import render_to_response

from application.models import Recipe, Ingredient
from application.watsonSearcher import watson_dir_search


# Create your views here.
def test(request):
    if request.method == 'GET':
        return render(request, 'homePage.html')
        
def example1(request):
    images_path = os.path.join('takeAdvantageOfYourFood', 'static', 'ingredientsImages')
    user_id = '18'
    recipe = watson_dir_search(images_path, user_id)[0]

    return get_recipe(request, recipe.recipe_id)
    
def example2(request):
    images_path = os.path.join('takeAdvantageOfYourFood', 'static', 'ingredientsImages')
    user_id = '32'
    recipe = watson_dir_search(images_path, user_id)[0]

    return get_recipe(request, recipe.recipe_id)

def get_recipe(request, recipe_id):
    print(recipe_id)
    if request.method == 'GET':
        try:

            recipe = Recipe.objects.get(recipe_id= recipe_id)
            ingredients = Ingredient.objects.filter(recipe=recipe)

        except:
            recipe = None
            ingredients = None

        return render(request, 'recipe.html', {'recipe': recipe, 'ingredients': ingredients})