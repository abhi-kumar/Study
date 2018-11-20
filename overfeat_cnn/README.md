# Overfeat CNN

[Source 1](https://vitalab.github.io/deep-learning/2017/04/18/overfeat.html), 

### 1.1 What constitutes overfeat CNN?
 - Used for obect localization and detection
 - Overfeat is a method that takes as input an image with one salient object and output the class of that object as well as its bounding box.
 - The network is a simple CNN but with 2 outputs : one for predicting the class score (softmax with cross-entropy loss) and one for predicting the bounding box coordinates (L2 loss).
 
  ![This is how the overfeat network looks](overfeat.jpg?raw=true "Overfeat network")
 
 - 
