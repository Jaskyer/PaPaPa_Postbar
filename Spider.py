#-*- coding:utf-8 -*-
import os
import re
import time
import urllib
import urllib2
import pineline
import config

ScriptPath = os.getcwd()
ActerFolder = config.acter
headers = config.headers

class SpiderWW(object):
    """
    Basic_url:初始页面URL
    URLs_Pool:主页所有的帖子的链接池
    folder:下载图片的文件夹名称
    """
    def __init__(self):
        self.Basic_url = config.url
        self.URLs_Pool = []
        self.folder = 1
		

    def Get_Basic_Html(self):
        """爬取首页所有帖子的URL，获取URL"""
        print u'获取到当前页URL为：%s\n' % self.Basic_url
        req = urllib2.Request(self.Basic_url,headers=headers)
        page = urllib2.urlopen(req)
        html = page.read()
        #获取该页所有帖子链接和该页的翻页链接
        (self.URLs_Pool,NextPage_Url) = pineline.Match_BasicURLs(html)
        print u'获取帖子链接成功！本页共帖子：%d\n' % len(self.URLs_Pool)
        #print self.URLs_Pool
        #print self.URLs_Pool.index('/p/4476033421')
        #if NextPage_Url is not False:
        #	self.Get_Basic_Html()
        #if NextPage_Url is False:
        #	print 'bbbbb'
        return 0

    def Get_Post_ImgURLs(self,PostUrl):
        """
        进入帖子,获取图片下载地址，进行图片下载
        PostUrl:帖子地址
        folderName:图片存放的文件夹名称
        DownLoadFlag:是否创建文件夹标志符，帖子没有图片可下载则置为0不创建，有则置为1
        """
        PostUrl = 'http://tieba.baidu.com%s' % PostUrl
        folderName = '%s/%d' % (ActerFolder,self.folder)
        DownLoadFlag = 0
        while True:
            print u'当前帖子URL：%s\n' % PostUrl
            time.sleep(5)
            print u'获取该页图片链接...\n'
            req = urllib2.Request(PostUrl,headers=headers)
            page = urllib2.urlopen(req)
            html = page.read()
            (ImgList,NextPage) = pineline.Match_ImgURL(html)
            ImgNum = len(ImgList)
            if(ImgNum == 0 and NextPage is False):
                print u'该页没有图片可以下载且已为最后一页！\n'
                break
            elif(ImgNum == 0 and NextPage is not False):
                print u'该页没有图片，进入下一页...\n'
                PostUrl = NextPage
                continue
            print u'获取图片链接成功！开始下载图片至文件夹：%s\n' % folderName
            CreateFolder(folderName,PostUrl)
            self.DownLoader(ImgList,folderName)
            DownLoadFlag = 1
            if NextPage is False:
            	print u'下载完毕！\n'
            	break
            PostUrl = NextPage
        if(DownLoadFlag == 1):
            self.folder = self.folder + 1
        print u'防止反爬虫，等待十秒继续...'
        time.sleep(10)
        return 0
        
     
    def DownLoader(self,Imglist,folderName):
        """下载该帖子的所有图片"""
        ImgName = 0
        for imgurl in Imglist:
            try:
            	time.sleep(0.5)
            	Piceure_Place = '%s\%s\%d_%d.jpg' % (ScriptPath,folderName,self.folder,ImgName)
                urllib.urlretrieve(imgurl,Piceure_Place)
            except Exception as e:
                print e
            ImgName = ImgName + 1
        print u'下载该贴图片完成！！\n'
        return 0
    
    def Run_Engine(self):
        """爬虫引擎，执行操作"""
        self.Get_Basic_Html()
        for url in self.URLs_Pool:
            print url
            self.Get_Post_ImgURLs(url)
        #self.DownLoader(img_list)
        
def CreateFolder(folderName,PostUrl):
    print u'检测文件夹%s是否存在...\n' % folderName
    FolderFlag = os.path.exists(folderName)
    print 'FloderFlag:%d' % FolderFlag
    if FolderFlag is False:
        os.mkdir(folderName)
        print u'文件夹%s不存在，创建文件夹成功...' % folderName
    FolderPath = ScriptPath + '/%s/url.txt' % (folderName)
    with open(FolderPath,'w') as f:
        content = '帖子链接为：%s' % PostUrl
        f.write(content)
    return 0





if __name__ == '__main__':
    print u'程序初始化...\n'
    WW = SpiderWW()
    CreateFolder(ActerFolder,WW.Basic_url)
    print u'初始化成功，程序开始运行...\n'
    WW.Run_Engine() 
    print u'所有图片下载完毕！'
#html = getHtml(url)
#IMG = getImg(html)
#print len(IMG)
#for rrr in IMG:
	#print rrr