#!usr/bin/env python
# coding=utf-8

#实现按主题划分找出关键字


'''
Created on 2016年6月7日
@author: hope.hou
'''


import os

info=u"E:/新建文件夹/过滤中文行"
#循环读取所有文件
if not os.path.exists(''+info+"/data"):
    os.makedirs(r''+info+"/data")
if not os.path.exists(''+info+"/conf"):
    os.makedirs(r''+info+"/conf")
if not os.path.exists(''+info+"/output"):
    os.makedirs(r''+info+"/output")


confdic={}
workfuncStr = ""
confFile = open(info+u"/conf/FuncTopic(技术类).txt")
confList = confFile.readlines( )
for line in confList:      
    line = line.replace('\n','').replace('\r','').replace('\t',' ').replace('\t','\t\t').replace("\xef\xbb\xbf","").strip()
    if line  == "":
        continue;   
    confdic[line.split()[0]] = line.split()[0:]    
    workfuncStr = workfuncStr+line+" "
workfuncList = workfuncStr.strip().split()
topicList = confdic.keys() 
print topicList
print workfuncList
#print confdic.values()
 
listfile=os.listdir(info+"/conf2")

str = ""

for item in listfile:      
    if item[-4:] == '.txt':
        readFile=open(info+"/conf2/"+item)                                          
        ori_words = readFile.readlines( ) 
        for line in ori_words: 
            line = line.replace('\n','').replace('\r','').replace('\t',' ').replace('\t','\t\t').replace("\xef\xbb\xbf","").strip()
            if line  == "":
                continue;    
                          
            for i in topicList:                                    
                if i != item[:-4]:   
                    continue
                str = str + line.split()[0]+ '\n'
                resultFile = open(info+"/output/"+item,'w')         
                resultFile.write(str+'\n')  
                resultFile.close()
        readFile.close()   
                    
print' '
print 'Well Done'
print u"结果保存路径为 ："+info+"/output/"
        
        





