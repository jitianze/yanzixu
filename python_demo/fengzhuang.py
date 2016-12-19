#!/usr/bin/env python
#-*-coding:utf-8-*-
class Person:
	name1 = "jitianze"
	name2 = "jiyubang"
	name3 = "qianbiao"
	def jyb(x):
		return x*2
	@staticmethod
	def jtz(y): 
		return y*2


if __name__ == "__main__":
	print Person.name1
	print Person.jtz(8)