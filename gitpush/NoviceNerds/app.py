# Importing libraries

from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report
from sklearn import metrics
from sklearn import tree
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv("Crop_recommendation.csv")
df.columns
df['label'].unique()
df['label'].value_counts()
numeric_df = df.select_dtypes(include='number')
sns.heatmap(numeric_df.corr(), annot=True)

features = df[['N', 'P','K','temperature', 'humidity', 'ph', 'rainfall']]
target = df['label']
labels = df['label']

acc = []
model = []

from sklearn.model_selection import train_test_split
Xtrain, Xtest, Ytrain, Ytest = train_test_split(features,target,test_size = 0.2,random_state =2)

#DECISION TREE
from sklearn.tree import DecisionTreeClassifier

DecisionTree = DecisionTreeClassifier(criterion="entropy",random_state=2,max_depth=5)

DecisionTree.fit(Xtrain,Ytrain)

predicted_values = DecisionTree.predict(Xtest)
x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('Decision Tree')
print("DecisionTrees's Accuracy is: ", x*100)

print(classification_report(Ytest,predicted_values))
from sklearn.model_selection import cross_val_score
# validation (decision tree)
score = cross_val_score(DecisionTree, features, target,cv=5)
score
import pickle

DT_pkl_filename = 'DecisionTree.pkl'

DT_Model_pkl = open(DT_pkl_filename, 'wb')
pickle.dump(DecisionTree, DT_Model_pkl)

DT_Model_pkl.close()

#guassian navie bayes
from sklearn.naive_bayes import GaussianNB

NaiveBayes = GaussianNB()

NaiveBayes.fit(Xtrain,Ytrain)

predicted_values = NaiveBayes.predict(Xtest)
x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('Naive Bayes')
print("Naive Bayes's Accuracy is: ", x*100)

print(classification_report(Ytest,predicted_values))
# validation (gnb)
score = cross_val_score(NaiveBayes,features,target,cv=5)
score
import pickle

NB_pkl_filename = 'NBClassifier.pkl'

NB_Model_pkl = open(NB_pkl_filename, 'wb')
pickle.dump(NaiveBayes, NB_Model_pkl)

NB_Model_pkl.close()

#SVM 
from sklearn.svm import SVC

SVM = SVC(gamma='auto')

SVM.fit(Xtrain,Ytrain)

predicted_values = SVM.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('SVM')
print("SVM's Accuracy is: ", x)

print(classification_report(Ytest,predicted_values))
#validation (SVM)
score = cross_val_score(SVM,features,target,cv=5)
score

#logistic regression
from sklearn.linear_model import LogisticRegression

LogRegres = LogisticRegression(random_state=2)

LogRegres.fit(Xtrain,Ytrain)

predict_values= LogRegres.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('Logistic Regression')
print("Logistic Regression's Accuracy is: ", x)

print(classification_report(Ytest, predicted_values))
#validation (logistic regression)
score = cross_val_score(LogRegres,features,target,cv=5)
score
import pickle

LR_pkl_filename = 'LogisticRegression.pkl'

LR_Model_pkl = open(DT_pkl_filename, 'wb')
pickle.dump(LogRegres, LR_Model_pkl)

LR_Model_pkl.close()

#random forest

from sklearn.ensemble import RandomForestClassifier

RanFor = RandomForestClassifier(n_estimators=20, random_state=0)
RanFor.fit(Xtrain,Ytrain)

predicted_values = RanFor.predict(Xtest)

x = metrics.accuracy_score(Ytest, predicted_values)
acc.append(x)
model.append('Random Forest')
print("Random Forest's Accuracy is: ", x)

print(classification_report(Ytest,predicted_values))
#validation (random forest)
score = cross_val_score(RanFor,features,target,cv=5)
score

import pickle

RF_pkl_filename = 'RandomForest.pkl'

RF_Model_pkl = open(RF_pkl_filename, 'wb')
pickle.dump(RanFor, RF_Model_pkl)

RF_Model_pkl.close()

plt.figure(figsize=[10,5],dpi = 100)
plt.title('Accuracy Comparison')
plt.xlabel('Accuracy')
plt.ylabel('Models Used')
sns.barplot(x = acc,y = model,palette='bright')

accuracy_models = dict(zip(model, acc))
for k, v in accuracy_models.items():
    print (k, '-->', v)

def pass_var(request):
    res=request.GET.get('data')
    data = np.array(res)
    prediction = RanFor.predict(data)
    print(prediction)