#!/usr/bin/env python
# -*- coding:utf-8 -*-

import urllib

req =urllib.urlopen('http://image21.360doc.com/DownloadImg/2010/12/2213/7871595_5.jpg')


# with open('meizi.jpg','wb') as f:
# 	f.write(jpg)


f =open('meinv.jpg','wb')
f.write(req.read())
f.close()

req.close()