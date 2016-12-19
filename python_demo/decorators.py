#!/usr/bin/env python
#-*-coding:utf-8-*-
def xuziyan(func):
	print 'woaixuziyan!'
	func()
	print 'xuziyanaiwo!'
	return func

def jtz():
	print 'xiangqinxiangai!'
jtz=xuziyan(jtz)
jtz()