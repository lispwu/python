# -*- coding:utf-8 -*-

import urllib
import urllib2
import re
import thread
import time

class QSBK:
    #初始化方法，定义一些变量
    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/4.0(compatible;MSIE 5.5;windows NT)'
        self.headers = {'User-Agent':self.user_agent}
        #存放段子的变量，每一个元素是每一页的段子
        self.stories = []
        #存放程序是否继续运行的变量
        self.enable = False

    #传入某一页的索引获得页面代码
    def getPage(self,pageIndex):
        try:
            url = 'http://www.qiushibaike.com/8hr/page/' + str(pageIndex)
            #构建请求
            request = urllib2.Request(url,headers=self.headers)
            #利用urlopen获取页面代码
            response = urllib2.urlopen(request)
            #将页面转化为utf-8编码
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接糗事百科失败，错误原因".e.reason
                return None

    #传入某一页代码，返回本页不带图片的段子列表
    def getPageItem(self,pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print "页面加载失败..."
            return None
        pattern = re.compile('h2>(.*?)</h2.*?span>(.*?)</.*?number">(.*?)</', re.S)
        items = pattern.findall(pageCode)
        pageStories = []
        for item in items:
            pageStories.append([item[0].strip(),item[1].strip(),item[2].strip()])
        return pageStories

    #加载并提取页面的内容，加入到列表中
    def loadPage(self):
        #如果当前未看的页数少于2页，则加载新一页
        if self.enable == True:
            if len(self.stories) < 2:
                pageStories = self.getPageItem(self.pageIndex)
                if pageStories:
                    self.stories.append(pageStories)
                    self.pageIndex += 1

    #调用该方法，每次敲回车打印一个段子
    def getOneStory(self,pageStories,page):
        for story in pageStories:
            input = raw_input()
            self.loadPage()
            if input == "Q":
                self.enable = False
                return
            print u"第%d页\t发布人：%s\t赞：%s\n%s" %(page,story[0],story[2],story[1])
    #开始方法
    def start(self):
        print u"正在读取糗事百科，按回车查看新段子，Q退出"
        self.enable = True
        self.loadPage()
        nowPage = 1
        while self.enable:
            if len(self.stories) > 0:
                pageStories = self.stories[0]
                nowPage += 1
                del self.stories[0]
                self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()
