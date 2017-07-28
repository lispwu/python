# -*- coding:utf-8 -*-

import urllib
import urllib2
import re

url = 'https://www.qiushibaike.com/text/'
user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;windows NT)'
headers = {'User-Agent':user_agent}

try:
    request = urllib2.Request(url,headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode('utf-8')
    print 'hi'
    pattern = re.compile('<a.*?content.*?<span>(.*?)</span>',re.S)
    print 'hi'
    items = re.findall(pattern,content)
    for item in items:
        print item[0]
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason
