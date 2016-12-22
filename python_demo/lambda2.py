#!/usr/bin/env python
# -*- coding:utf-8 -*-
def a(x):
    return lambda y:x+y
    
    # return lambda x:x+y 如果这样写那么第二次它的y就找不到了 会报错

print a(10)(20)

# 方便 灵活 简洁 快速  java python 痛苦 python java 你会java 渣 
# 奇葩 但是这个写很灵活 


b =a(10)
print b(20)