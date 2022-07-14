from sklearn import metrics, svm
from sklearn.ensemble import RandomForestClassifier

train_data=[[0,0],[0,1],[1,0],[1,1]]
train_label=[0,1,1,0]
test_data=[[0,0],[1,0]]
test_label=[0,1]

clf_svm=svm.SVC()
clf_rf=RandomForestClassifier()
clf_svm.fit(train_data,train_label)
clf_rf.fit(train_data,train_label)
result_svm=clf_svm.predict(test_data)
result_rf=clf_rf.predict(test_data)
print("svm: ",result_svm)
print("rf: ", result_rf)


score_svm=metrics.accuracy_score(test_label,result_svm)
score_rf=metrics.accuracy_score(test_label,result_rf)
score=clf_svm.score(test_data,test_label)
print('svm 정확도:',score_svm)
print('svm',score)
print('rf 정확도:',score_rf)