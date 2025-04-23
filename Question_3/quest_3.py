"""
QUESTION 1

You have trained a linear regression model, and you notice the following:
The model performs very well on the training set but poorly on the validation set
The predictions on the validation set are highly sensitive to small changes in the input data (high variance)
The model seems to be overfitting
Which regularization technique would help reduce the variance and prevent overfitting in this scenario?
L1 regularization (Lasso)
L2 regularization (Ridge)

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




"""