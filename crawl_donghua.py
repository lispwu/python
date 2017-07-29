# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib
import re

class ECUT:
    def __init__(self):
        self.loginUrl = "https://cas.ecit.cn/index.jsp"
        self.cookies = cookielib.CookieJar()
        self.postdata = urllib.urlencode({
            'username':'201320080230',
            'password':'7758258'
        })
        self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
    def getPage(self):
        request = urllib2.Request(
            url = self.loginUrl,
            data = self.postdata
        )
        result = self.opener.open(request)
        print result.read().decode('gbk')

ecut = ECUT()
ecut.getPage()
