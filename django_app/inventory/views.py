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
	try:
		template="home.html"
		user_id = request.GET["user_id"]
		user = User.objects.get(pk=user_id)
		purchases = PurchaseHistory.objects.filter(user=user)
		skus = Sku.objects.all()
		return render(request,template,{"skus":skus,"purchases":purchases,"user_id":user_id})
	except Exception,e:
		raise Http404
def save(request):
	pass