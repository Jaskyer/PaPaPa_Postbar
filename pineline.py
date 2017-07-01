# -*- coding:utf-8 -*-
import os
import re
import urllib

def Match_BasicURLs(html):
    """
    传入html,匹配首页，获取初始页的URL集，送入URL池，获取下一页的URL
    NextPage_enable默认为0，为0时返回URL集合与下一页的URL
    NextPage_Enable为0时只返回URL集合"""
    #PostUrl为匹配主页上的所有帖子的链接URL：
    reg_PostUrl = r'<a href="(/p/.*)" title="'
    imgre1 = re.compile(reg_PostUrl)
    PostUrl_List = re.findall(imgre1,html)
    #print u'解析该页共有帖子数：%d\n' % len(PostUrl_List)

    #NextPage为主页的翻页的链接URL
    reg_NextPage = r'<a href="(.+?)" class="next pagination-item " >下一页&gt;</a>'
    imgre2 = re.compile(reg_NextPage)
    next_page = re.search(imgre2,html)
    if next_page is not None:
        Next_Page = 'http:%s' % next_page.group(1)
        print u'解析到该页的翻页链接为：%s\n' % Next_Page
    else:
        Next_Page = False
        print u'已经到了最后一页！Next_Page返回值：False\n'
    
    return PostUrl_List,Next_Page

def Match_ImgURL(html):
    """匹配获取每页的图片URL，送给DownLoader下载"""
    reg_img = r'(?<=<img class="BDE_Image" src=").+?\.jpg(?=" size=)'
    imgre1 = re.compile(reg_img)
    imglist = re.findall(imgre1,html)
    print u'解析到该帖子共有可下载图片数：%d' % len(imglist)
    print imglist

    reg_NextPage = r'<a href="(.+?)">下一页</a>'
    imgre2 = re.compile(reg_NextPage)
    next_page = re.search(imgre2,html)
    print u'\n检测是否有下一页...\n'
    if next_page is not None:
        Next_Page = 'http://tieba.baidu.com%s' % next_page.group(1)
        print u'检测到该页的翻页链接为：%s\n' % Next_Page
    else:
        Next_Page = False
        print u'已经到了最后一页！Next_Page返回值：False\n'
    
    return imglist,Next_Page


def Match_Post_NextPage(html):
    """获取具体某个帖子的下一页(翻页)"""
    