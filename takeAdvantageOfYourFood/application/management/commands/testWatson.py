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
import json
import os
from os import listdir
from os.path import isfile, join

from django.core.management.base import BaseCommand
from watson_developer_cloud import VisualRecognitionV3
from application.models import Recipe, Ingredient

class Command(BaseCommand):

	def testWatson(self):
		visual_recognition = VisualRecognitionV3(
			'2018-03-19',
			url='https://gateway.watsonplatform.net/visual-recognition/api',
			iam_apikey=os.environ.get('WATSON_API_KEY'))
		
		user_id = '18'
		images_path = os.path.join('takeAdvantageOfYourFood', 'static', 'ingredientsImages', user_id)
		images_files = [f for f in listdir(images_path) if isfile(join(images_path, f))]
		#print(images_files)
		ingredients_results = self.get_watson_ingredients_results(visual_recognition, images_path, images_files)
		print(ingredients_results)

		recipes = Recipe.objects.filter(ingredients_quantity= len(ingredients_results))
		#print(recpies[0].name)

		for recipe in recipes:
			i = 0
			for ingredient_result in ingredients_results:
				for ingredient in ingredient_result:
					if len(Ingredient.objects.filter(recipe= recipe, ingredient_name__contains= ingredient)) != 0:
						i += 1
						break
			if len(ingredients_results) == i:
				print("{\"ID\": "+str(recipe.recipe_id)+", \"Name\": \""+recipe.name+"\"}")

	def get_watson_ingredients_results(self, visual_recognition, images_path, images_files):
		ingredients_results = []

		for image_file in images_files:
			with open(os.path.join(images_path,image_file), 'rb') as images_file:
				classes = visual_recognition.classify(
					images_file,
					threshold='0.85',
					classifier_ids='food').get_result()
				
				results = classes["images"][0]["classifiers"][0]["classes"]
				#print(json.dumps(results, indent=2))

				ingredient_results = []

				for result in results:
					ingredient_results.append(result["class"])

				#print(ingredient_results)
				ingredients_results.append(ingredient_results)

		return ingredients_results

	def handle(self, *args, **options):
		self.testWatson()