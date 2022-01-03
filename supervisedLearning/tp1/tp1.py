from scipy import linalg
import numpy as np
import pylab as pl
import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
from sklearn.manifold import TSNE
from sklearn.preprocessing import LabelEncoder


df = pd.read_csv("iris.csv")

#visualisation
xv = df.drop("variety", axis=1)
tsne = TSNE(n_components=2)
embedding = tsne.fit_transform(xv)
le = LabelEncoder()
y = le.fit_transform(df.variety)

# plt.scatter(*embedding.T, c=y)
# plt.show()

#calcul de la moyenne 

data = df.to_numpy()

mean0 = np.empty([4,1])
mean1 = np.empty([4,1])
mean2 = np.empty([4,1])

len0 = 0
len1 = 0
len2 = 0

print("before :" + str(data))
print(y)
for index,row in enumerate(data):
    if y[index] == 0:
        len0 += 1
        for i in range(4):
            mean0[i] += row[i]

    if y[index] == 1:
        len1 += 1
        for i in range(4):
            mean1[i] += row[i]

    if y[index] == 2:
        len2 += 1
        for i in range(4):
            mean2[i] += row[i]

mean0 /= len0
mean1 /= len1
mean2 /= len2

print(len0)
print(len1)
print(len2)

print("Moyenne 0 : " + str(mean0))
print("Moyenne 1 : " + str(mean1))
print("Moyenne 2 : " + str(mean2))

# calcul de Sw

sw0 = np.empty([4, 4])
sw1 = np.empty([4, 4])
sw2 = np.empty([4, 4])


for index,row in enumerate(data):
    if y[index] == 0:
        for i in range(4):
            print(row[i], mean0[i])
            sw0[i] += (row[i]-mean0[i]) * (row[i]-mean0[i]).T

    if y[index] == 1:
        for i in range(4):
            sw1[i] += (row[i]-mean1[i]) * (row[i]-mean1[i]).T

    if y[index] == 2:
        for i in range(4):
            sw2[i] += (row[i]-mean2[i]) * (row[i]-mean2[i]).T

print("sw0 :" + str(sw0))
print("sw1 :" + str(sw1))
print("sw2 :" + str(sw2))
   


