#!usr/bin/env python
# coding=utf-8
'''
Created on 2016年6月5日

@author: lenovo
'''

from util.FileUtil import *

info=u"E:/新建文件夹/新建文件夹"
dic = readKeyValueFileToDic(info+"/dic.txt")
print dic


oriFile = open(info+"/a.txt")
topics = open(info+'/result.txt','w')   
topics2 = open(info+'/result2.txt','w')   

ori_words = oriFile.readlines( )
for line in ori_words:        
    line = line.replace('\n','').replace('\r','').replace('\t',' ').replace('\t','\t\t').replace("\xef\xbb\xbf","").strip()
    if line  == "":
        continue;   
    
    keylistName = ""
    keylistCode = line.split(' ')
    for key in keylistCode:
        keylistName = keylistName + dic[key] + ' '
    #print line+' '+keylistName
    r = line+' '+keylistName+'\n'
    topics.write(r)
    topics2.write(keylistName+'\n')
  
topics.close()
topics2.close()

print 'ok'
print u"结果保存路径为 ："+info+"/result1.txt"
        
        





