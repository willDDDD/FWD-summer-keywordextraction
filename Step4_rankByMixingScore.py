# sort terms based on the different mixed score
import json
with open("joinTwoScore.txt", 'r', encoding='utf-8') as file2:    # from previous
    res_ = file2.readlines()
target2 = open("test.txt", 'w',encoding='utf-8')  # file to store result

i = 0
while i < len(res_):
    res_[i] = res_[i].split('\t')
    res_[i][2] = res_[i][2].strip('\n')
    if 'e' in res_[i][2]:
        res_[i][2] = 0
    res_[i].append(str(float(res_[i][1])*(1/16) + float(res_[i][2]) * (15/16)))   # res_[i][1] is for important score and res_[i][2] is for relevance score. You can change (1/16) and (15/16) to other number in order to rank terms in different mixing score
    i+=1


res_.sort(key = lambda x: x[3],reverse=True) # rank terms based on new mixing score

for i in range(len(res_)):
    target2.write(str(res_[i][0]) + '\t' +str(res_[i][3]) + '\t' + str(res_[i][1]) + '\t' + str(res_[i][2]) + "\n")
target2.close()
print('done')

