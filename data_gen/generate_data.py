#!/usr/bin/python

import ConfigParser
import MySQLdb

import sys
import os
import random


class GenerateData():

	def __init__(self):
		config = ConfigParser.RawConfigParser()
		config.read('settings.ini')

		self.dbname = config.get('database','database.dbname')
		host = config.get('database','database.host')
		port = config.get('database','database.port')
		user = config.get('database','database.user')
		passwd = config.get('database','database.passwd')

		self.dbConnection = MySQLdb.connect(host=host,port=int(port),
			user=user,passwd=passwd,db=self.dbname)

		self.grocery = config.get("files","grocerylist")
		self.sku = config.get("files","skulist")

	def done(self):
		cur = self.dbConnection.cursor()
		
		INSERT_QUERY = "INSERT INTO inventory_product(name,category,group_by) values('%s','%s','%d');"
		for line in open(self.grocery):
			[name,category,group] = [x.strip() for x in line.split(",")]
			group_t = 0;
			if group== 'true':
				group_t = 1
			print INSERT_QUERY%(name,category,group_t)
			cur.execute(INSERT_QUERY%(name,category,group_t))
		cur.close()
		self.dbConnection.commit()
		
		cat_dict = {}
		for line in open(self.sku):
			[category,a,b,q]= [x.strip() for x in line.split(",")]
			cat_dict[category] = [a,b,q]


		cur1 = self.dbConnection.cursor()
		cur1.execute("select * from inventory_product");
		rows = cur1.fetchall()
		cur1.close()

		cur = self.dbConnection.cursor()
		INSERT_QUERY = "INSERT INTO inventory_sku(quantity,type_quantity,product_id) values ('%s','%s','%d')"
		for row in rows:
			product_id = row[0]
			category = row[2]
			l = cat_dict[category]
			print INSERT_QUERY%(l[0],l[2],product_id)
			print INSERT_QUERY%(l[1],l[2],product_id)
			cur.execute(INSERT_QUERY%(l[0],l[2],product_id))
			cur.execute(INSERT_QUERY%(l[1],l[2],product_id))
		cur.close()
		self.dbConnection.commit()
		





if __name__ == '__main__':
	genData = GenerateData()
	genData.done()