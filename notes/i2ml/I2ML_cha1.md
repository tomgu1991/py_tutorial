# Chapter1

### Terminology

Machine **learning** is about extracting knowledge from data.

The most successful kind of machine learning algorithms are those that automate a decision making processes by generalizing from known examples. In this setting, which is known as a **supervised learning** setting, the user provides the algorithm with pairs of inputs and desired outputs, and the algorithm finds a way to produce the desired output given an input.

The other type of algorithms that we will cover in this book is unsupervised algorithms. In **unsupervised learning**, only the input data is known and there is no known output data given to the algorithm. While there are many successful applications of these methods as well, they are usually harder to understand and evaluate.

Each entity or row here is known as data point or **sample** in machine learning, while the columns, the properties that describe these entities, are called **features**. Building a good representation of your data, which is called **feature extraction** or feature engineering.

Since we have measurements for which we know the correct species of iris, this is a supervised learning problem. In this problem, we want to predict one of several options (the species of iris). This is an example of a **classiication** problem. The possible outputs (different species of irises) are called **classes**. The desired output for a single data point (an iris) is the species of this flower. For a particular data point, the species it belongs to is called its **label**. Remember that the individual items are called samples in machine learning, and their properties are called features.

Unfortunately, we can not use the data we use to build the model to evaluate it. This is because our model can always simply remember the whole training set, and will therefore always predict the correct label for any point in the training set. This “remembering” does not indicate to us whether our model will **generalize** well, in other words whether it will also perform well on new data. So before we apply our model to new measurements, we will want to know whether we can trust its predictions. The part of the data is used to build our machine learning model, and is called the **training data or training set**. The rest of the data will be used to access how well the model works and is called **test data, test set or hold-out set**.

A **scatter plot** of the data puts one feature along the x-axis, one feature along the y-
axis, and draws a dot for each data point.

Here we will use a **k-nearest neighbors classifier**, which is easy to understand. Building this model only consists of storing the training set. To make a prediction for a new data point, the algorithm finds the point in the training set that is closest to the new point. Then it assigns the label of this training point to the new data point. The k in k-nearest neighbors signifies that instead of using only the closest neighbor to the new data point, we can consider any fixed number k of neighbors in the training (for example, the closest three or five neighbors). 

### Code

```python
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
```

