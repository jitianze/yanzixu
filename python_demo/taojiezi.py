#!/usr/bin/env python
#-*- coding:utf-8 -*-
import socket

#socket.socket() 此为创建套接字的方法
print socket.gethostname() #获取主机名
print socket.gethostbyname(socket.gethostname()) #获取电脑ip
print socket.gethostbyname_ex(socket.gethostname())
s= socket.socket()
host="www.baidu.com"
port=443
s.connect((host,port))
s.send("nihao")
baner=s.recv(1024)
if baner:
	print baner
