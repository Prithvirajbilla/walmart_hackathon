from django.db import models

# Create your models here.

class Product(models.Model):
	name = models.CharField(max_length=128,db_index=True)
	category = models.CharField(max_length=128,db_index=True)

	def __str__(self):
		self.name

class Sku(models.Model):
	product = models.ForeignKey(Product)
	quantity = models.IntegerField()
	type_quantity = models.CharField(max_length=10)


class User(models.Model):
	user_name = models.CharField(max_length=128)
	last_updated = models.DateTimeField()

class PurchaseHistory(models.Model):
	user = models.ForeignKey(User)
	sku = models.ForeignKey(Sku)
	purchase_datetime = models.DateTimeField()
	pruchase_time = models.TimeField()

class Predictions(models.Model):
	user = models.ForeignKey(User)
	category = models.CharField(max_length=128)
	predicted_datetime = models.DateTimeField()
	predicted_time = models.TimeField()
