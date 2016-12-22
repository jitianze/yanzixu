#!/usr/bin/env python
#-*-coding:utf-8-*-
class Person:
	name = None
	gender = None

	def __init__(self,name,gender):

		self.name = name
		self.gender = gender

	def self_introduction(self):

		print "my name is",self.name
		print "I am ",self.gender

	def __del__(self):
		print self.name,"is shen"

		
if __name__ == '__main__':

	tp=Person("jitianze","nan")
	tp.self_introduction()



	del tp	
