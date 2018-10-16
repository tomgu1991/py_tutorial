# Chapter2_1&2

### Terminology

There are two major types of supervised machine learning problems, called **classification** and **regression**.

In **classification**, the goal is to predict a **class** label, which is a choice from a predefined list of possibilities.

Classification is sometimes separated into binary classification, which is the special case of distinguishing between exactly **two classes**, and **multiclass classification**, which is classification between more than two classes.

For **regression** tasks, the goal is to predict a **continuous number, or a floating-point number** in programming terms (or real number in mathematical terms). Predicting a person’s annual income from their education, their age, and where they live is an example of a regression task. When predicting income, the predicted value is an amount, and can be any number in a given range. Another example of a regression task is predicting the yield of a corn farm given attributes such as previous yields, weather, and number of employees working on the farm. The yield again can be an arbitrary number.

An easy way to distinguish between classification and regression tasks is to ask whether there is some kind of **continuity** in the output. If there is continuity between possible outcomes, then the problem is a regression problem.

If a model is able to make accurate predictions on unseen data, we say it is able to **generalize** from the training set to the test set. We want to build a model that is able to generalize as accurately as possible.

Building a model that is too complex for the amount of information we have, as our novice data scientist did, is called **overfitting**. Overfitting occurs when you fit a model too closely to the particularities of the training set and obtain a model that works well on the training set but is not able to generalize to new data. On the other hand, if your model is too simple—say, “Everybody who owns a house buys a boat”—then you might not be able to capture all the aspects of and vari‐ ability in the data, and your model will do badly even on the training set. Choosing too simple a model is called **underfitting**.

 Usually, collecting more data points will yield more variety, so larger datasets allow building more complex models. However, simply duplicating the same data points or collecting very similar data will not help.

For two-dimensional datasets, we can also illustrate the prediction for all possible test points in the xy-plane. We color the plane according to the class that would be assigned to a point in this region. This lets us view the **decision boundary**, which is the divide between where the algorithm assigns class 0 versus where it assigns class 1.

