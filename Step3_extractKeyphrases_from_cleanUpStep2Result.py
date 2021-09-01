# extract keyphrases
import json
with open(r'C:\Users\Downloads\cleanUpStep2.txt', 'r', encoding='utf-8') as file2:    # the result from cleanUpStep2Result
    res_ = file2.readlines()

target2 = open("keyphrasesFromAutophrases.txt", 'w',encoding='utf-8') #file to store result
for i in range(len(res_)):
    res_[i] = res_[i].split('\t')
    res_[i][1] = res_[i][1].strip(' ')
    res_[i][1] = res_[i][1].strip('\n')
    target2.write("\"" + res_[i][1]+"\"" + "," + "\n")
target2.close()
print("done")

