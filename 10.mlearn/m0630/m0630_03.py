import glob,os.path,re
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier

def makeData(url):        
    files = glob.glob(url)
    data=[]
    label=[]

    for file in files:
        basename= os.path.basename(file)
        lang = basename.split('-')[0]

        with open(file,'r',encoding='utf-8') as f:
            text=f.read()
            text=text.lower()
        code_a=ord('a')
        code_z=ord('z')
        count = [0 for n in range(26)]
        for ch in text:
            code_current=ord(ch)
            if code_a <= code_current <= code_z:
                count[code_current- code_a] += 1
                
        total = sum(count)
        count= list(map(lambda n:n/total,count))      
        data.append(count)
        label.append(lang)
    return data,label
url='10.mlearn/m0630/test/*.txt'
url1='10.mlearn/m0630/train/*.txt'
url2='10.mlearn/m0630/train_test/fr-100.txt'

train_x,train_y=makeData(url)
test_x,test_y=makeData(url1)
test_x1,test_y1=makeData(url2)
print(test_x1)

clf=RandomForestClassifier()
# clf=svm.SVC()
clf.fit(train_x,train_y)
pred=clf.predict(test_x1)
# score=clf.score(test_x,test_y)
print('예측: ',pred)
# print('정확도: ',score)