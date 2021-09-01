import json
import random
import pandas as pd
import numpy as np
import scipy.stats as scs

db = pd.read_csv('math_keys.csv',sep='\t',names=['words'])  # math keyword list for calculating precision rate
wordlist=db['words']
words = []
for i in wordlist:
    words.append(i.lower())

### cs keyword list for calculating precision rate
# db = pd.read_csv(r'C:\Users\Xiuhao Ding\Downloads\Keywords-Springer-83K-20210405.csv',sep='\t',names=['words','freq'])
# wordlist=db['words']
# words = []
# for i in wordlist:
#     temp = i.split(',')[0].lower()
#     words.append(temp)
    
with open("test.txt", 'r', encoding='utf-8') as file2:    # ranking terms based on mixing score, which is the result of Step4_rankByMixingScore.py
    res_ = file2.readlines()

i = 0                   ## situation1: i = 0. Calculate the top (i_upper) presicion rate in test.txt.
i_lower = i-0          ## situation2: i = k and i_upper = k+m. Calculate the "k to (k+m)" precision rate in test.txt
i_upper = 1000
count = 0
avg = 0
while i < i_upper:
    res_[i] = res_[i].split('\t')
    
    flag1 = 0
    flag2 = 0
    for j in words:
        if res_[i][0] in j:
            flag1 = 1
            break
        if j != '' and j in res_[i][0] and len(j.split(' ')) > 1:
            flag2 = 1
            break

    if flag1 == 1 or flag2 == 1 or res_[i][0] in words:
        avg += float(res_[i][2])
        count+=1
    i+=1
print("avg important score for the true precise terms" + ":" + str(avg / count))  # avg important score for the true precise terms
print( "count of true precise terms" + ":" + str(count))      
print("precision rate" + ":" + str(count/(i_upper - i_lower)))# precision rate

