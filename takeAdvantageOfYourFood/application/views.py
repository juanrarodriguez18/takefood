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
from django.core.paginator import Paginator
from django.shortcuts import render
from django.shortcuts import render_to_response

from application.models import Recipe, Ingredient


# Create your views here.
def test(request):
    if request.method == 'GET':
        return render(request, 'homePage.html')
        
def example1(request):
    None
    
def example2(request):
    None