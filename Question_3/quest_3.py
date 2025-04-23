"""
QUESTION 1

You have trained a linear regression model, and you notice the following:
The model performs very well on the training set but poorly on the validation set
The predictions on the validation set are highly sensitive to small changes in the input data (high variance)
The model seems to be overfitting
Which regularization technique would help reduce the variance and prevent overfitting in this scenario?
L1 regularization (Lasso)
L2 regularization (Ridge)
============================================
ANSWER:

where the linear regression model is overfitting, shows high variance,
and performs poorly on the validation set—the best regularization technique to help reduce variance and prevent overfitting is:
***** L2 regularization (Ridge) *****

EXPLANATION:

Why Ridge (L2)?
L2 regularization adds a penalty equal to the square of the magnitude of coefficients.
It shrinks the coefficients smoothly toward zero, helping to reduce model complexity without making any of them exactly zero.
This smooth shrinkage is effective in reducing variance, which is exactly the problem in your case.

About L1 (Lasso):
L1 regularization (Lasso) tends to produce sparse models by setting some coefficients exactly to zero.
It's great when you want feature selection,
but it may not be as effective as L2 in reducing variance when overfitting is the main issue.
*********************************************************************************************
*********************************************************************************************

QUESTION 2:

You are working with a linear regression model that includes many input features,
and you suspect that some features are irrelevant (they contribute little to the prediction).
You want to:
Reduce the number of features used by the model
Encourage the model to automatically set some coefficients to zero (effectively removing those features)
Which regularization method should you use?
L1 regularization (Lasso)
L2 regularization (Ridge)
===============================================

ANSWER:

where you want to reduce the number of features and have the model automatically
set some coefficients to zero—the best regularization technique is:
***** L1 regularization (Lasso) *****

EXPLANATION:

L1 regularization adds a penalty equal to the absolute value of the coefficients.
It has the effect of shrinking some coefficients exactly to zero,
which effectively removes those features from the model.
This makes it ideal for feature selection, especially when you suspect that some features are irrelevant.

About L2 (Ridge)?
L2 regularization shrinks coefficients toward zero, but never exactly to zero.
It helps reduce overfitting, but it does not perform feature selection.
"""