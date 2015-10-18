from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
import json
import datetime
import urllib 
from inventory.models import *

def user_select(request):
	template= "user_select.html"
	users = User.objects.all()
	return render(request,template,{"users":users})



def home(request):
	template="home.html"
	skus = Sku.objects.all()
	return render(request,template,{"skus":skus})