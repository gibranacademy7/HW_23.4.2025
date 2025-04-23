"""
in the following graph:


Questions:

1. where is the underfit? where is the overfit?
2. where is the ideal area?
3. use the dotted line in your answer, i.e. left to the dotted line

Answers:

1. Underfitting happens left to the first dotted line, where both training and test errors are high.
The model is too simple to capture the underlying patterns in the data.

2. Overfitting occurs right to the second dotted line, where training error is very low,
but test error starts increasing. The model is too complex and fits the training data too closely,
including noise.

3. The ideal area is between the two dotted lines, where the model has low training and test errors.
This is the optimal balance between bias and variance.
"""