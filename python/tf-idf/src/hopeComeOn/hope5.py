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
 
listfile=os.listdir(info+"/conf1")
count = 0
for item in listfile:  
    
    if item[-4:] == '.txt':
        for i in workfuncList:            
            if i == item[:-4]:                      
                count +=1
                readFile=open(info+"/conf1/"+item)
                resultFile = open(info+"/conf2/"+item,'w') 
                                 
                ori_words = readFile.readlines( ) 
                print item
                print ori_words
                print "*********"
                for line in ori_words:        
                    line = line.replace('\n','').replace('\r','').replace('\t',' ').replace('\t','\t\t').replace("\xef\xbb\xbf","").strip()
                    if line  == "":
                        continue;  
                    print line    
                    resultFile.write(line+'\n') 
                     
                readFile.close()                 
                resultFile.close()                       
                
                
                
      

print' '
print str(count) + '文件已处理完毕'
print 'Well Done'
print u"结果保存路径为 ："+info+"/conf2/"
        
        





