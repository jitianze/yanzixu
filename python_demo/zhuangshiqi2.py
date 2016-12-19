#!/usr/bin/env python
#-*-coding:utf8-*-
def zsq(func):
	def _zsq(*args,**kw):
		print "zhe shi zhuangshi de content!"
		result=func(*args,**kw)
		print result
		print "zhe shi zhuangshi de content2 !"
		return result
	return _zsq

@zsq
def hanshu(x,y):
	return x+y
print hanshu(1,2)
print hanshu(0,344)