from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
import json
import urllib 
from inventory.models import *
from datetime import datetime
import datetime as dt
from collections import Counter
import requests
import json



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
		user = User.objects.get(pk=user_id)
		user.last_updated =datetime.now()
		user.save()
		purchase = PurchaseHistory(user=User.objects.get(pk=user_id),
			sku=Sku.objects.get(pk=sku_id),purchase_datetime=t_datetime,purchase_time=t_time)
		purchase.save()
		
		return HttpResponseRedirect("/purchase_history?user_id="+user_id)
	except Exception, e:
		raise

def predict(request,uid):
	try:
		template = "predict.html"
		user = User.objects.get(pk=uid)
		last_activity = user.last_updated

		predictions = Predictions.objects.filter(user=user)

		run_pred = False

		if len(predictions) > 0:
			if predictions[0].created_time < last_activity:
				for pred in predictions:
					pred.delete()
				run_pred = True

		if run_pred:
			purchases = PurchaseHistory.objects.filter(user=user).order_by('purchase_datetime')
			pred_dict = {}
			pred_dict_qnt = {}
			new_predict_time = []
			for purchase in purchases:
				cat_name = ""
				if purchase.sku.product.group_by:
					cat_name = purchase.sku.product.category
				else:
					cat_name = purchase.sku.product
				if cat_name in pred_dict:
					pred_dict[cat_name].append(purchase.purchase_datetime)
					pred_dict_qnt[cat_name].append(purchase.sku.quantity)
				else:
					pred_dict[cat_name] = [purchase.purchase_datetime]
					pred_dict_qnt[cat_name] = [purchase.sku.quantity]

				new_predict_time.append(purchase.purchase_time.hour)

			print pred_dict

			new_predict = {}
			last_purchase = {}

			for key in pred_dict:
				m = min(pred_dict_qnt[key])

				if len(pred_dict[key]) > 1:
					new_predict[key] = []

					for i in range(len(pred_dict[key])-1):
						d = (pred_dict[key][i+1]-pred_dict[key][i]).days
						qnty = pred_dict_qnt[key][i]
						new_predict[key].append(d*m/qnty)
					last_purchase[key] = pred_dict[key][-1]


			print new_predict,new_predict_time,last_purchase
			most_common,num_most_common = Counter(new_predict_time).most_common(1)[0]
			print most_common,num_most_common

			for key in new_predict:
				days_now = sum(new_predict[key])/len(new_predict[key])
				if days_now != 0:
					cur_prediction = Predictions(user=user,
						category=key,
						predicted_datetime=last_purchase[key]+dt.timedelta(days=days_now),
						predicted_time=dt.time(most_common,0,0),created_time=datetime.now())
					cur_prediction.save()

			predictions = Predictions.objects.filter(user=user)

		print predictions
		return render(request,template,{"predictions":predictions,"user_id":uid})
	except Exception, e:
		raise e

def token(request):
	token = request.GET["token"]
	user_name = request.GET["user"]
	if User.objects.filter(token=token).count() == 0:
		User(token=token,user_name=user_name,last_updated=dt.datetime.now()).save()
	return HttpResponse("hello")

def push(request,uid,pid):
	try:
		url= "https://gcm-http.googleapis.com/gcm/send"
		headers = {'Content-Type': 'application/json','Authorization':'key=AIzaSyC4r57hIzGbmTZQfh31_w1p5fOon0GMpBc'}
		user = User.objects.get(pk=uid)
		prediction = Predictions.objects.get(pk=pid)
		payload = {}
		payload["to"] = user.token
		payload["data"] = {"category":prediction.category}
		requests.post(url,headers=headers,data=json.dumps(payload))

		return HttpResponseRedirect("/predict/"+uid+"/")

	except Exception,e:
		print  e
		return HttpResponseRedirect("/predict/"+uid+"/")

