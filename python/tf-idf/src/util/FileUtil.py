#
#1. the file must be stored as utf-8
#2. the file is like: 1 a
#
def readKeyValueFileToDic(filePath):
    dic={}
    dicFile = open(filePath)
    dic_words = dicFile.readlines( )
    for line in dic_words:        
        line = line.replace('\n','').replace('\r','').replace('  ',' ').replace('\t\t','\t').replace("\xef\xbb\xbf","").strip()
        if line  == "":
            continue;    
        arr=line.split(' ')
        dic[arr[0]] = arr[1]
    return dic

