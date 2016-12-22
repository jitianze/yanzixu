#!/usr/bin/env python	
#-*-coding:utf-8-*-
def jia(x,y):
	return x+y
def jian(x,y):
	return x-y
def chu(x,y):
	return x/y
def cheng(x,y):
	return x*y
operate={'+':jia,'-':jian,'/':chu,'*':cheng}
def jisuanji(x,y,z):
	return operate.get(z)(x,y)

print jisuanji(20,4,'+')
print jisuanji(20,4,'-')
print jisuanji(20,4,'/')
print jisuanji(20,4,'*')