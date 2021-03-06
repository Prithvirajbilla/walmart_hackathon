from django.db import models

# Create your models here.
from django.utils import timezone

class Product(models.Model):
	name = models.CharField(max_length=128,db_index=True)
	category = models.CharField(max_length=128,db_index=True)
	group_by = models.BooleanField(default=False)

	def __str__(self):
		return self.name

	def __unicode__(self):
		return self.name


class Sku(models.Model):
	product = models.ForeignKey(Product)
	quantity = models.IntegerField()
	type_quantity = models.CharField(max_length=10)

	def __str__(self):
		return (self.product.name+" (%s) [%d %s]")%(self.product.category,self.quantity,self.type_quantity)

	def __unicode__(self):
		return (self.product.name+" (%s) [%d %s]")%(self.product.category,self.quantity,self.type_quantity)


class User(models.Model):
	user_name = models.CharField(max_length=128)
	last_updated = models.DateTimeField()
	token = models.CharField(max_length=256)

	def __str__(self):
		return self.user_name

	def __unicode__(self):
		return self.user_name

class PurchaseHistory(models.Model):
	user = models.ForeignKey(User)
	sku = models.ForeignKey(Sku)
	purchase_datetime = models.DateTimeField()
	purchase_time = models.TimeField()

	def __str__(self):
		return (self.sku.product.name+" (%s) [%d %s]")%(self.sku.product.category,self.sku.quantity,
			self.sku.type_quantity)

	def __unicode__(self):
		return (self.sku.product.name+" (%s) [%d %s]")%(self.sku.product.category,self.sku.quantity,
			self.sku.type_quantity)


class Predictions(models.Model):
	user = models.ForeignKey(User)
	category = models.CharField(max_length=128)
	predicted_datetime = models.DateTimeField()
	predicted_time = models.TimeField()
	created_time = models.DateTimeField()
