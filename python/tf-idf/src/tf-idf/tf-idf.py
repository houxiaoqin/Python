#!usr/bin/env python
# coding=utf-8

"""idf-ok.py -- this is a idf algorithm demo
@version: 1.0
@author:Bin Xu and hope
@see:
"""

from __future__ import division
import os
import sys
import math

info="E:/workspace/TF-IDF/text_data"

# 数据结构
#统计词语出现次数
word_nums = {}
# 文章所有的单词数量
all_nums = 0
# 停用词统计
stop_word = []

# 统计的总文章数量
all_doc_num = 0
# 文章中单词的总数: 文件名-所有出现的单词
doc_words_map = {}
# 出现的所有单词-set
doc_all_word = []

# 初始化目录
if not os.path.exists(''+info+"/data"):
    os.makedirs(r''+info+"/data")
if not os.path.exists(''+info+"/conf"):
    os.makedirs(r''+info+"/conf")
if not os.path.exists(''+info+"/output"):
    os.makedirs(r''+info+"/output")

listfile=os.listdir(info+"/data")
# --------------

# 读stop_word文件
stopWordFile = open(info+"/conf/stop_word.txt")
all_stop_words = stopWordFile.readlines( )
for line in all_stop_words:
    if line.strip() == '':
        continue
    line = line.replace('\n',' ').replace('\r',' ')
    stop_word.append(line.strip())
# ---------------------

for item in listfile:  
    if item[-4:] == '.txt':
        all_doc_num += 1
        readFile=open(info+"/data/"+item)
        all_the_text = readFile.readlines( )
        doc_words = []
        for line in all_the_text:
            if line.strip() == '':
                continue
            line = line.replace('\n',' ').replace('\r',' ')
            # 处理词语进行统计 ------------------------------
            words = line.split(" ")
            for word in words:
                if word.strip() == '':
                    continue
                if stop_word.count(word)>0:
                    continue
                
                if word_nums.has_key(word):
                    word_nums[word] = word_nums[word]+1
                else:
                    word_nums[word] = 1
                
                # 所有参与统计的单词数量统计
                all_nums += 1
                
                #  单个文档的所有单词统计
                if doc_words.count(word) == 0:
                    doc_words.append(word)
                
                if doc_all_word.count(word) == 0:
                    doc_all_word.append(word)
        doc_words_map[item] = doc_words #文章中所有的单词
        readFile.close()
        #  ----------------------------------------------------
        # 统计单词出现的文章数量
        
#print "输出的结果："
#print word_nums
print u"单词数量："+str(all_nums)
# 保存数据
print u"总文件数："+str(all_doc_num)
print u"单词统计的数量："+str(word_nums)
word_nums = sorted(word_nums.iteritems(), key=lambda d:d[1], reverse = True)
print u"单词统计排序后的数量："+str(word_nums)
print u"每个文档中的单词统计："+str(doc_words_map)
print u"不重复所有词语："+str(doc_all_word)

# 计算-某个词语出现在多个文档中
word_doc_number = {}
for word in doc_all_word:
    word_doc_num = 0
    for doc_word in doc_words_map:
        words = doc_words_map[doc_word]
        if words.count(word)>0:
            word_doc_num += 1
    word_doc_number[word] = word_doc_num
    
print u"单词出现的文档数"+str(word_doc_number)    

out_put_tf = open(info+"/output/result.idf","w")
for work in word_nums:
    tf = work[1]/all_nums
    
    idf = math.log(all_doc_num/word_doc_number[work[0]])
    tf_idf = tf * idf
    # msg =  work[0]  + "\t" + str(work[1]) + "\t" + str(tf) +"\t" +str(idf)+"\t" +str(tf_idf)+"\t"+str(all_doc_num)+"\t"+str(word_doc_number[work[0]]) + "\n"
    msg =  work[0]  + "\t" + str(idf) + "\n"
    print msg
    out_put_tf.write(msg)
out_put_tf.close()
    
    
    
    
    
    
    
    
    


