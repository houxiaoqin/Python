#!usr/bin/env python
# coding=utf-8
'''
Created on 2016年6月5日

@author: lenovo
'''

from util.FileUtil import *

info=u"E:/新建文件夹/新建文件夹"
oriFile = open(info+"/a.txt")
dic = readKeyValueFileToDic(info+"/dic.txt")
print dic
