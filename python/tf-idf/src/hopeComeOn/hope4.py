#!usr/bin/env python
# coding=utf-8
'''
Created on 2016年6月7日

@author: hope.hou
'''
#按业务需求批量处理hope3.py
import os

info=u"E:/新建文件夹/过滤中文行"
#循环读取所有文件
if not os.path.exists(''+info+"/data"):
    os.makedirs(r''+info+"/data")
if not os.path.exists(''+info+"/conf"):
    os.makedirs(r''+info+"/conf")
if not os.path.exists(''+info+"/output"):
    os.makedirs(r''+info+"/output")
listfile=os.listdir(info+"/conf1")
count = 0
dic={}
for item in listfile:      
    count +=1
    if item[-4:] == '.txt':
        readFile=open(info+"/conf1/"+item)
        
        ori_words = readFile.readlines( )
        #print ori_words        
        print '**************'
        print '== file'+str(count)+" " +item +' begins:'
        
        for line in ori_words:        
            line = line.replace('\n','').replace('\r','').replace('\t',' ').replace('\t','\t\t').replace("\xef\xbb\xbf","").strip()
            if line  == "":
                continue;  
            #print line.split()
            dic[line.split()[0]] = line.split()[1]
        readFile.close()


        

resultFile = open(info+'/output/allkeywords.txt','w')              
for keywords in dic.keys():
    #print keywords+'/n' 
    resultFile.write(keywords+'/n'+'\n') 
resultFile.close()


print' '
print 'Well Done'
print u"结果保存路径为 ："+info+"/output/"
        
        





