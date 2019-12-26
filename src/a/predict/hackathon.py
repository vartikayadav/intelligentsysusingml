
import pandas as pd
import numpy as np


trdf = pd.read_csv('C:\\traffic_pred\\src\\a\\predict\\train_aWnotuB.csv')
trainMat = trdf.as_matrix()
tedf = pd.read_csv('C:\\traffic_pred\\src\\a\\predict\\test_BdBKkAj.csv')
testMat = tedf.as_matrix()
train = []
target = []
#print(trainMat)
for i in trainMat:
    s = i[3]
    year = s / (10**7)
    s = s % (10**7)
    month = s / (10**5)
    s = s % (10**5)
    date = s / (10**3)
    s = s % (10**3)
    time = s / (10)
    s = s % (10)
    junction = s
    train.append([year, month, date, time, junction])
    target.append(i[2])
X = np.array(train)
y = np.array(target)
#print(X)
#print(y)
jun1 = []
jun2 = []
jun3 = []
jun4 = []
jun5 = []
jun = [jun1, jun2, jun3, jun4, jun5]
for i in range(0,len(train), 24):
    ct = 0
    for j in range(24):
        ct += target[i+j]#gives no of vehicles passed in a day and keep count of total
    #print(ct)
    #print train[i][4]
    jun[train[i][4]-1].append(ct)#append count of vehicles passed in jun for coressponding days
#print(len(jun[0]))
#print(len(jun[3]))
#print(jun[3])
jun[3] = [0]*(len(jun[0])- len(jun[3])) + jun[3]
#print(jun[3])
#print(len(jun[0]), len(jun[1]), len(jun[2]), len(jun[3]))

k = 7
week = [[] for i in range(k)]
for i in range(len(jun[1])):
    week[i%k].append(jun[1][i])
#for i in range(k):
 #   print(np.mean(week[i]))


hour = [[] for i in range(24)]
for i in range(len(jun[0])*24+len(jun[1])*24, len(jun[0])*24+len(jun[1])*24+len(jun[2])*24):
    hour[i%24].append(target[i])

#for i in range(24):
 #   print(np.mean(hour[i]))

temp = [-i for i in jun[3]]
jun[4] = np.add(jun[2], temp)
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(10,10))

plt.plot(jun[0], 'red')
f1=fig.savefig('C:\\traffic_pred\\src\\a\\static\\images\\plot1.png')

plt.plot(jun[1], 'blue')
f2=fig.savefig('C:\\traffic_pred\\src\\a\\static\\images\\plot2.png')


plt.plot(jun[2], 'green')
f3=fig.savefig('C:\\traffic_pred\\src\\a\\static\\images\\plot3.png')


plt.plot(jun[3], 'yellow')
f4=fig.savefig('C:\\traffic_pred\\src\\a\\static\\images\\plot4.png')


#plt.plot(jun[4], 'red')
#f5=fig.savefig('C:\\traffic_pred\\src\\a\\static\\images\\plot5.png')



from sklearn.model_selection import StratifiedKFold
skf = StratifiedKFold(n_splits=7)
from sklearn.ensemble import RandomForestClassifier
clf1 = RandomForestClassifier(criterion = 'entropy', min_samples_split = 150, min_samples_leaf = 10, max_depth = 12, class_weight = 'balanced', n_estimators = 100)
from sklearn.linear_model import LinearRegression
clf2 = LinearRegression()
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.metrics import mean_squared_error
from math import sqrt

'''
for train_index, test_index in skf.split(X, y):
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    clf2 = clf1.fit(X_train, y_train)
    pred2 = clf1.predict(X_test)
    print pred1[:10], y_test[:10]
    rms = sqrt(mean_squared_error(y_test, pred2))
    print rms'''

#clf2 = clf2.fit(X, y)
#pred = clf2.predict(X)
clf2 = clf2.fit(X, y)
pred = clf2.predict(X)
print(pred)
rms=np.sqrt(np.mean(np.power((y-pred),2)))

def fun():
    return ((clf2,pred,rms))
k=fun()
