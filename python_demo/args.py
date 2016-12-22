#!/usr/bin/env python	
#-*-coding:utf-8-*-
def hanshu(x,y,*args):
	print x,y,args
hanshu(1,2,3)

hanshu(1,2,3,4,5,6,5,7,8,9)
#hanshu(1)  传一个参数会报错！
hanshu(1,2,[1,2,3,4,5,6,7,8,9])
def xuziyan(*args):
	print args
xuziyan(0)
# *args输出为一个元组 谨记
#**args传递的是关键词参数（即字典形式），输出为一个字典！
