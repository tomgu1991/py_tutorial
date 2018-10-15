#!/usr/bin/env python3
# Author Zuxing Gu

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, colorConverter, LinearSegmentedColormap
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# create color
cm3 = ListedColormap(['#0000aa', '#ff2020', '#50ff50'])

# load data
iris_data = load_iris()

# learn data features
print("iris_key:\n{}".format(iris_data.keys()))
#print(iris_data['DESCR'])
print(iris_data['data'].shape)
'''
dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names'])
data: (150,4)
target: 0 1 2 -> setosa versicolor virginica
feature_names -> sepal length, sepal width, petal length, petal width
'''

# split training set and test set
X_train, X_test, y_train, y_test = train_test_split(iris_data['data'], iris_data['target'], random_state=0)
print("X_train shape:", X_train.shape)
print("y_train shape:", y_train.shape)

# look at data
# create dataframe from data in X_train
# label the columns using the strings in iris_dataset.feature_names
iris_dataframe = pd.DataFrame(X_train, columns=iris_data.feature_names)
# create a scatter matrix from the dataframe, color by y_train
'''
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.plotting.scatter_matrix.html
pandas.plotting.scatter_matrix(frame, alpha=0.5, figsize=None, ax=None, grid=False, diagonal='hist', marker='.', 
density_kwds=None, hist_kwds=None, range_padding=0.05, **kwds)
'''
pd.plotting.scatter_matrix(iris_dataframe, c=y_train, figsize=(15, 15),
                           marker='o', hist_kwds={'bins': 20}, s=60,
                           alpha=.8, cmap=cm3)

#plt.show()

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

# make prediction for one test
X_new = np.array([[5, 2.9, 1, 0.2]])
print("X_new:{}".format(X_new))
prediction = knn.predict(X_new)
print("Prediction:", prediction)
print("Predicted target name:",
       iris_data['target_names'][prediction])

# result for test_set
y_pred = knn.predict(X_test)
print("Test set predictions:\n", y_pred)
print("Test set score: {:.2f}".format(np.mean(y_pred == y_test)))