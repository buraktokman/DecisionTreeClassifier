#!/usr/bin/env python
from sklearn import tree
features = [[140, 1], [130, 1], [150, 0], [170, 0]] #scikit-learn  uses real-values [0, 1, ...]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[160, 0]]))

'''
Table for Training Data

Weight  #Texture    #Label
150g    Bumpy       Orange
170g    Bumpy       Orange
140g    Smooth      Apple
130g    Smooth      Apple

Think features as the input to the classifier, label as the output.
0 = Bumpy, 1 = Smooth
0 = Apple, 1 = Orange

Decision tree
                Weight >= 150g ?
                Yes    /\   No
    Texture = Bumpy ?
        Yes   / \   No
     Orange        Apple

'''
