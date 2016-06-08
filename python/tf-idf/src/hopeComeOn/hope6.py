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
#workfuncStr = ""
confFile = open(info+u"/conf/FuncTopic(技术类).txt")
confList = confFile.readlines( )
countElementInListDic={}
for line in confList:      
    line = line.replace('\n','').replace('\r','').replace('\t',' ').replace('\t','\t\t').replace("\xef\xbb\xbf","").strip()
    if line  == "":
        continue;   
    #print line
    #print len(line.split())
    
    countElementInListDic[line.split()[0]] = len(line.split())
    confdic[line.split()[0]] = line.split()
print countElementInListDic
    #workfuncStr = workfuncStr+line+" "
#workfuncList = workfuncStr.strip().split()
topicList = confdic.keys() 
print topicList
#print workfuncList
print confdic.values()
 
listfile=os.listdir(info+"/conf2")

count = 0
strTopic = ""
dic = {}
for item in listfile:      
    if item[-4:] == '.txt':
        readFile=open(info+"/conf2/"+item)  
        ori_words = readFile.readlines( ) 
                                                
        
        print '******'
        count += 1
        print count
        print 'Next file begins:'
        
         
        
    
        for topicCode in topicList:
            
            
            #strTopic = ""
            
            for fileNameInTheSameTopic in confdic[topicCode]:  
                if fileNameInTheSameTopic != item[:-4]:
                    continue                                                
                
                print "topicCode:"+topicCode+" 该主题下的所有职能如下："
                print confdic[topicCode]
                print '扫描文件'+ fileNameInTheSameTopic +'。txt'
                
                str = ""  
                for line in ori_words: 
                    line = line.replace('\n','').replace('\r','').replace('\t',' ').replace('\t','\t\t').replace("\xef\xbb\xbf","").strip()
                    if line  == "":
                        continue;                       
                    str = str +line.split()[0]+" " 
                                    
                                        
                print str
                strTopic = strTopic + str +" "
                #print strTopic
                countElementInListDic[topicCode] -=1                
                
                resultFile = open(info+"/output/"+topicCode+'.txt','w')
                if countElementInListDic[topicCode]==0:
                    print '该主题 ok'
                    print list(set(strTopic.strip().split()))
                    for line2 in list(set(strTopic.strip().split())):                                              
                               
                        resultFile.write(line2+'\n') 
                        print line2 
                        
                        
                    print 'OK'
                    strTopic = " "
readFile.close()                    
resultFile.close()                       
 
print' '
print 'Well Done'
print u"结果保存路径为 ："+info+"/output/"
        
        





