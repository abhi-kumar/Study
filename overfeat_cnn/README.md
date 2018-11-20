# Overfeat CNN

[Source 1](https://vitalab.github.io/deep-learning/2017/04/18/overfeat.html), [Source 2](https://arxiv.org/pdf/1312.6229.pdf), [Source 3](https://medium.com/coinmonks/review-of-overfeat-winner-of-ilsvrc-2013-localization-task-object-detection-a6f8b9044754),


### 1.1. What constitutes overfeat CNN?
 - Used for obect localization and detection
 - Overfeat is a method that takes as input an image with one salient object and output the class of that object as well as its bounding box.
 - The network is a simple CNN but with 2 outputs : one for predicting the class score (softmax with cross-entropy loss) and one for predicting the bounding box coordinates (L2 loss).
 
  ![This is how the overfeat network looks](overfeat.png?raw=true "Overfeat network")
 
 - In order to improve precision, the network processes several sliding windows (at multiple resolution), each sliding window having a class score and a bounding box.

### 1.2. A few points from paper
 - show that different tasks can be learned simultaneously using a single shared network.
 - main point of the paper is to show that training a convolutional network to simultaneously classify, locate and detect objects in images can boost the classification accuracy and the detection and  localization accuracy of  all  tasks.
 - apply a ConvNet at multiple locations  in  the  image,  in  a  sliding  window fashion,  and  over multiple  scales.

### 1.3. How are the models
 - The classification model
   - is same as alexnet, with a few changes. 
     - no local contrast normalization (LRN)
     - pooling layers are non-overlapping
     - first and second layers use smaller strides of 2
   - has fine stride pooling in 5th layer
     - 3×3 max pooling is done for multiple times with different pixel offset, Δx and Δy, from {0, 1, 2}
     - results in 9 pooled feature maps in total.
   - takes input image with six scales
   - during test time, FC layer becomes 1x1 conv layer
 
  - Regression model
    - Used for obect position detection
    - the network augments (or branches out of) classification model
      - connected at the 5th layer of the CNN. 
      - 2 FC layers (4096 and 1024 sizes) are used to have regression prediction of coordinates for the bounding box edges.
      - 1st layer of the regression net is connected to a 5×5 spatial neighborhood in the layer 5 maps, as well as all 256 channels.
      - 2nd regression layer has 1024 units and is fully connected.
    
    
    
    
    
