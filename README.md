# Decision Tree Classifier

Tutorial for Decision Tree Classifier with scikit-learn
Based on the [Hello World - Machine Learning Recipes #1](https://www.youtube.com/watch?v=cKxRvEZd3Mw)

## Summary

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