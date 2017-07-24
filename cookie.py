import urllib2
import cookielib

filename = 'cookie.txt'
#声明一个cookieJar对象实例来保存cookie
cookie = cookielib.MozillaCookieJar(filename)

#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)

#通过handler来构建opener
opener = urllib2.build_opener(handler)

response = opener.open('http://www.baidu.com')

cookie.save(ignore_discard=True,ignore_expires=True)