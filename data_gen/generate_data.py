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
			user=user,passwd=passwd)

		self.csvfile = config.get("files","csv")

	def done(self):
		pass



if __name__ == '__main__':
	genData = GenerateData()
	genData.done()