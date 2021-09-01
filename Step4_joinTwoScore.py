# Join important score and relevance score
import json
with open("output.txt", 'r', encoding='utf-8') as file2:    #output from domain relevance measure, containing relevance score
    res_ = file2.readlines()
with open("cleanUpStep2.txt", 'r', encoding='utf-8') as file3:    #result of Autophrases,containing important score
    s = file3.readlines()
target2 = open("joinTwoScore.txt", 'w',encoding='utf-8') #file to store result


i = 0
while i < len(res_):
    res_[i] = res_[i].split(':')
    res_[i][1] = res_[i][1].strip(' ')
    res_[i][1] = res_[i][1].strip('\n')
    i+=1

m = 0
while m < len(s):
    s[m] = s[m].split('\t') 
    s[m][1] = s[m][1].strip(' ')
    s[m][1] = s[m][1].strip('\n')
    m+=1
            
for i in range(len(s)):
    target2.writelines(s[i][1] + '\t' + s[i][0] + '\t' + res_[i][1]  + '\n')


target2.close()
print('done')

