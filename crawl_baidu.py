# -*- coding:utf-8 -*-
__author__ = 'WS'

import urllib
import urllib2
import re

#处理页面标签
class Tool:
    # 去除img标签,7位长空格
    removeImg = re.compile('<img.*?>| {7}|')
    # 删除超链接标签
    removeAddr = re.compile('<a.*?>|</a>')
    # 把换行的标签换为\n
    replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # 将表格制表<td>替换为\t
    replaceTD = re.compile('<td>')
    # 把段落开头换为\n加空两格
    replacePara = re.compile('<p.*?>')
    # 将换行符或双换行符替换为\n
    replaceBR = re.compile('<br><br>|<br>')
    # 将其余标签剔除
    removeExtraTag = re.compile('<.*?>')

    def replace(self,x):
        x = re.sub(self.removeImg,"",x)
        x = re.sub(self.removeAddr,"",x)
        x = re.sub(self.replaceLine, "\n", x)
        x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n    ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        # strip()将前后多余内容删除
        return x.strip()


class BDTB:
    #初始化，传入基地址，是否看楼主的参数
    def __init__(self,baseUrl,seeLZ):
        self.baseURL = baseUrl
        self.seeLZ = "?see_lz=" + str(seeLZ)
        self.tool = Tool()
    #传入页码，获取该页帖子的代码
    def getPage(self,pageNum):
        try:
            url = self.baseURL + self.seeLZ +"&pn=" + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            print 'hi1'
            return response.read().decode("utf-8")
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败，错误原因",e.reason
                return None
    #获取帖子标题
    def getTitle(self):
        page = self.getPage(1)
        print 'hi2'
        pattern = re.compile('<h3 class=core_title_txt.*?>(.*?)</h3>', re.S)
        result = re.search(pattern,page)
        if result:

            return result.group(1).strip()
        else:
            return None

    #获取帖子的页数
    def getPageNum(self):
        page = self.getPage(1)
        #这个页数到底是如何确定的？通过标签里的共几页确定的
        pattern = re.compile('<li class=l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        result = re.search(pattern,page)
        if result:
            print result
            return result.group(1).strip()
        else:
            return None

    #获取每一层楼的内容，传入页面内容
    def getContent(self,page):
        print 'hi3'
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        items = re.findall(pattern,page)
        print 'hi4'
        for item in items:
            print 'hi5'
            print item

baseURL = "http://tieba.baidu.com/p/3138733512"
bdtb = BDTB(baseURL,1)
bdtb.getContent(bdtb.getPage(1))



