from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
import json
import urllib 
from inventory.models import *
from datetime import datetime


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
	try:
		user_id = request.POST["user_id"]
		sku_id = request.POST["sku_id"]
		purchased_datetime = request.POST["purchased_datetime"]
		t_datetime = datetime.strptime(purchased_datetime, '%m/%d/%Y %I:%M %p')
		t_time = t_datetime.time()
		purchase = PurchaseHistory(user=User.objects.get(pk=user_id),
			sku=Sku.objects.get(pk=sku_id),purchase_datetime=t_datetime,purchase_time=t_time)
		purchase.save()
		
		return HttpResponseRedirect("/purchase_history?user_id="+user_id)
	except Exception, e:
		raise