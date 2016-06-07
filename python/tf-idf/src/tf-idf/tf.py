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

text_length=0
word_count = {}
word_idf = {} #idf权重记录

info="E:/workspace/TF-IDF/text_data"
f = open(info+"/predict/t.txt")
texts = f.readlines( )
for line in texts:
    
    if line.strip() == '':
        continue
    line = line.strip().replace('\n',' ').replace('\r',' ')     # 换行符
    word_arr=line.split(" ")    
    text_length += len(word_arr)
    
    for c in word_arr:
        if word_count.has_key(c):
            word_count[c] += 1
        else:
            word_count[c] = 1
            
print word_count
print text_length


f = open(info+"/output/result.idf")
texts = f.readlines( )
for line in texts:
    line = line.strip().replace('\n',' ').replace('\r',' ') 
    word = line.split('\t')    #\t制表符
    word_idf[word[0]] = word[1]   
      
tf_idf_sorted={}   
for word in word_count:
    tf =  word_count[word] / text_length
    idf = 1
    if word_idf.has_key(word):
        idf = word_idf[word]   
    tf_idf = float(tf) * float(idf)
    #print word + '\t' +str(tf_idf)
    tf_idf_sorted[word] = tf_idf 

tf_idf_sorted = sorted(tf_idf_sorted.iteritems(), key=lambda d:d[1], reverse = True)
    
print tf_idf_sorted
# php

 
        
    
    
       
# ---------------------

