#!/usr/bin/env python3
# Author Zuxing Gu

import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split

import mglearn

X, y = mglearn.datasets.make_wave(n_samples=60)
plt.plot(X, y, 'bo')
plt.show()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

'''
# linear regression
lr = LinearRegression().fit(X_train, y_train)
print("lr.coef_: {}".format(lr.coef_))
print("lr.intercept_: {}".format(lr.intercept_))
# lr.coef_: [0.39390555]
# lr.intercept_: -0.031804343026759746
print("Training set score: {:.2f}".format(lr.score(X_train, y_train)))
print("Test set score: {:.2f}".format(lr.score(X_test, y_test)))
# Training set score: 0.67
# Test set score: 0.66 -> underfit
print("x = 0, y_pre is " + lr.predict(0))
# -0.03180434
'''

# ridge regression
'''
ridge = Ridge().fit(X_train, y_train)
print("lr.coef_: {}".format(ridge.coef_))
print("lr.intercept_: {}".format(ridge.intercept_))
# lr.coef_: [0.39390555]
# lr.intercept_: -0.031804343026759746
print("Training set score: {:.2f}".format(ridge.score(X_train, y_train)))
print("Test set score: {:.2f}".format(ridge.score(X_test, y_test)))
# Training set score: 0.67
# Test set score: 0.66 -> underfit
print("x = 0, y_pre is {}".format(ridge.predict(0)))
# -0.03180434
'''

'''
ridge10 = Ridge(alpha=10).fit(X_train, y_train)
print("lr.coef_: {}".format(ridge10.coef_))
print("lr.intercept_: {}".format(ridge10.intercept_))
print("Training set score: {:.2f}".format(ridge10.score(X_train, y_train)))
print("Test set score: {:.2f}".format(ridge10.score(X_test, y_test)))
print("x = 0, y_pre is {}".format(ridge10.predict(0)))
'''
'''
lr.coef_: [0.36940192]
lr.intercept_: -0.03922685902991124
Training set score: 0.67
Test set score: 0.64
x = 0, y_pre is [-0.03922686]
'''

'''
ridge01 = Ridge(alpha=0.1).fit(X_train, y_train)
print("lr.coef_: {}".format(ridge01.coef_))
print("lr.intercept_: {}".format(ridge01.intercept_))
print("Training set score: {:.2f}".format(ridge01.score(X_train, y_train)))
print("Test set score: {:.2f}".format(ridge01.score(X_test, y_test)))
print("x = 0, y_pre is {}".format(ridge01.predict(0)))
'''
'''
lr.coef_: [0.39364443]
lr.intercept_: -0.03188343931569505
Training set score: 0.67
Test set score: 0.66
x = 0, y_pre is [-0.03188344]
'''

# Lasso
from sklearn.linear_model import Lasso

lasso = Lasso().fit(X_train, y_train)
print("lr.coef_: {}".format(lasso.coef_))
print("lr.intercept_: {}".format(lasso.intercept_))
print("Training set score: {:.2f}".format(lasso.score(X_train, y_train)))
print("Test set score: {:.2f}".format(lasso.score(X_test, y_test)))
print("Number of features used: {}".format(np.sum(lasso.coef_ != 0)))
'''
lr.coef_: [0.09540593]
lr.intercept_: -0.12222434377983978
Training set score: 0.29
Test set score: 0.24
Number of features used: 1
'''

lasso001 = Lasso(alpha=0.01, max_iter=100000).fit(X_train, y_train)
print("lr.coef_: {}".format(lasso001.coef_))
print("lr.intercept_: {}".format(lasso001.intercept_))
print("Training set score: {:.2f}".format(lasso001.score(X_train, y_train)))
print("Test set score: {:.2f}".format(lasso001.score(X_test, y_test)))
print("Number of features used: {}".format(np.sum(lasso001.coef_ != 0)))
'''
lr.coef_: [0.39092055]
lr.intercept_: -0.03270854303429055
Training set score: 0.67
Test set score: 0.66
Number of features used: 1
'''
