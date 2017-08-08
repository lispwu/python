# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

class DB:

    def __init__(self):
        self.pageNum = 0
        self.baseURL = 'https://www.douban.com/doulist/3936288/?start={pageNum}&sort=time&sub_type='
        self.user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        self.headers = {'User-Agent': self.user_agent}

    def getPage(self):
        try:
            url = self.baseURL
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            return response.read().decode('utf-8')
        except urllib2.URLError,e:
            if hasattr(e,'reason'):
                print u'连接豆瓣失败',e.reason
                return None



    def getContent(self,page):
        pattern = re.compile('_blank">(.*?)</a>.*?rating_nums">(.*?)</span>.*?abstract">(.*?)</div>')
        items = re.findall(pattern,page)
        for item in items:
            print item[0],item[1],item[2]

    def start(self):
        page = self.getPage()
        content = self.getContent(page)



db = DB()
db.start()
