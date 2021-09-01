# clean up the result from step2, excluding the terms including symbols
import json
with open(r'C:\Users\\Desktop\AutoPhrase.txt', 'r', encoding='utf-8') as file2:    # AutoPhrase/models/DBLP/AutoPhrase.txt
    res_ = file2.readlines()
e = ["\\", "~", "$", "_", "-", "*", ":"]  #exclude terms incuding symbols
target2 = open("cleanUpStep2.txt", 'w',encoding='utf-8') # file to store the result
for i in range(len(res_)):
    check = 0
    for E in e:
        if E in res_[i][13:-1]:
            check = 1
            break
    if check == 1:
        continue
    target2.write(res_[i][0:12] + '\t' +res_[i][13:-1]+ "\n")
target2.close()
print("done")

