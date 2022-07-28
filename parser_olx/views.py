from distutils.log import error
from itertools import product
from django.shortcuts import render, redirect
from .parser import main_parse
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from .models import Product, Category
from django.contrib.auth import authenticate, login as auth_login
import json
from datetime import datetime
from django.core import serializers


# Create your views here.
def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def main(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    if is_ajax(request) and request.method == "GET":
        
        #products = serializers.serialize('json', Product.objects.all() )   #тут по вкусу, можно все объекты, можно частями.
        #return HttpResponse(products, content_type='application/json')
        context={"data":Product.objects.all()}
        template = "product_block.html"
        return render(request, template, context)

    
    context={}
    template = "main.html"
    return render(request, template, context)

def login(request):
    nick_name = ""
    error = ""
    if request.method == "POST":
        nick_name = request.POST.get("nickname")
        password  = request.POST.get("password")
        print(nick_name)
        print(nick_name)

        user = authenticate(username=nick_name, password=password)
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                #return HttpResponse('Authenticated successfully')
                return redirect("main")
        else:
            #return HttpResponse('Перевірте дані та спробуйте ще раз!')
            error = "Помилка введених даних"
            print("Перевірте дані та спробуйте ще раз!")
            error = "Перевірте дані та спробуйте ще раз!"

    context={"error":error}
    template = "login.html"
    return render(request, template, context)





        
