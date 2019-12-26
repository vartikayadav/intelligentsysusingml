import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

trdf = pd.read_csv('C:\\traffic_pred\\src\\a\\predict\\train_aWnotuB.csv')
trainMat = trdf.as_matrix()
tedf = pd.read_csv('C:\\traffic_pred\\src\\a\\predict\\test_BdBKkAj.csv')
testMat = tedf.as_matrix()

#print(trainMat[:10])
#print("hi")
#print(testMat[:10])

def plot_graph(mat):
    y_axis = [j[-2] for j in mat]
    y_new = []
    for i in range(len(y_axis)):
        if y_axis[i]:
            plt.plot(y_axis)
    plt.show()


split_juction_1=[]
split_juction_2=[]
split_juction_3=[]
split_juction_4=[]

for row in trainMat:
    if row[1] == 1:
        split_juction_1.append(row.tolist())
    elif row[1] == 2 :
        split_juction_2.append(row.tolist())
    elif row[1] == 3:
        split_juction_3.append(row.tolist())
    else:
        split_juction_4.append(row.tolist())

plot_graph(split_juction_1)
plot_graph(split_juction_2)
plot_graph(split_juction_3)
plot_graph(split_juction_4)

def get_data_month(mat,month):
    new_mat = []
    for row in mat:
        if int(row[0][5:7]) == month:
            new_mat.append(row.tolist())
    return new_mat

mat_month=[]
for i in range(1,13):
    mat_month.append((get_data_month(trainMat,i)))

for rw in mat_month:
    plot_graph(rw)
