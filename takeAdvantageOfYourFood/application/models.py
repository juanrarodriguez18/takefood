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
from __future__ import unicode_literals

from django.db import models

class Recipe(models.Model):
    recipe_id = models.IntegerField()
    name = models.CharField(max_length=100)
    ease_of_prep = models.CharField(max_length=100)
    recipe_type = models.CharField(max_length=100)
    prep_time = models.IntegerField(default=0)
    photo = models.URLField()
    ingredients_quantity = models.IntegerField()
    link = models.URLField()

    def __unicode__(self):
        return self.name+" ("+str(self.recipe_id)+")"


class Ingredient(models.Model):
    ingredient_name = models.CharField(max_length=100)
    recpie = models.ForeignKey(Recipe, on_delete=models.CASCADE, blank=True, null=True)

    def __unicode__(self):
        return self.ingredient_name
