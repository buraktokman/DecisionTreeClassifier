# Decision Tree Classifier

Tutorial for Decision Tree Classifier with scikit-learn<br>
Based on the [Hello World - Machine Learning Recipes #1](https://www.youtube.com/watch?v=cKxRvEZd3Mw)

## Summary<br>

Table for Training Data<br>
Weight  #Texture    #Label<br>

150g    Bumpy       Orange<br>
170g    Bumpy       Orange<br>
140g    Smooth      Apple<br>
130g    Smooth      Apple<br>

Think features as the input to the classifier, label as the output.<br>
0 = Bumpy, 1 = Smooth<br>
0 = Apple, 1 = Orange<br>

Decision tree<br>
                Weight >= 150g ?<br>
                Yes    /\   No<br>
    Texture = Bumpy ?<br>
        Yes   / \   No<br>
     Orange        Apple<br>
