#!usr/bin/env python
# coding=utf-8
'''
Created on 2016年6月5日

@author: lenovo
'''

from util.FileUtil import *
import re


def is_chinese(uchar):
#判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True           
    else:
        return False
#===============================================================================
# if is_chinese(u'语言'):
#     print u'中文'
# print type(u'语言')
#===============================================================================

info=u"E:/新建文件夹/过滤中文行"
oriFile = open(info+"/test.txt")
resultFile = open(info+'/result_ChineseLinesDeleted.txt','w')  
ori_words = oriFile.readlines( )

for line in ori_words:        
    line = line.replace('\n','').replace('\r','').replace('\t',' ').replace('\t','\t\t').replace("\xef\xbb\xbf","").strip()
    if line  == "":
        continue; 
#===
    line_unicode = unicode(line, "utf-8")
    if is_chinese(line_unicode):
        continue
    resultFile.write(line+'\n') 
    print line
#===
   
oriFile.close()
resultFile.close()

print 'ok'
print u"结果保存路径为 ："+info+"/result_ChineseLinesDeleted.txt"
        
        





