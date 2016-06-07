#!usr/bin/env python
# coding=utf-8


#实现批量处理hope2.py



'''
Created on 2016年6月5日

@author: lenovo
'''

from util.FileUtil import *
import re
import os



def is_chinese(uchar):
#判断一个unicode是否是汉字"""
    if uchar >= u'\u4e00' and uchar<=u'\u9fa5':
        return True           
    else:
        return False
#===============================================================================
# 示例：
# if is_chinese(u'语言'):
#     print u'中文'
# print type(u'语言')
#===============================================================================

info=u"E:/新建文件夹/过滤中文行"
#循环读取所有文件
if not os.path.exists(''+info+"/data"):
    os.makedirs(r''+info+"/data")
if not os.path.exists(''+info+"/conf"):
    os.makedirs(r''+info+"/conf")
if not os.path.exists(''+info+"/output"):
    os.makedirs(r''+info+"/output")
listfile=os.listdir(info+"/data")
count = 0
for item in listfile:  
    count +=1
    if item[-4:] == '.txt':
        readFile=open(info+"/data/"+item)
        resultFile = open(info+"/output/"+item,'w')  
        ori_words = readFile.readlines( )
        #print ori_words        
        print '**************'
        print '== file'+str(count)+' begins:'
        
        for line in ori_words:        
            line = line.replace('\n','').replace('\r','').replace('\t',' ').replace('\t','\t\t').replace("\xef\xbb\xbf","").strip()
            if line  == "":
                continue;  
            #print line
#===
            line_unicode = unicode(line, "utf-8")
            if is_chinese(line_unicode):
                continue
            #print line
            resultFile.write(line+'\n') 

#===
   

#resultFile.close()
print' '
print 'Well Done'
print u"结果保存路径为 ："+info+"/output/"
        
        





