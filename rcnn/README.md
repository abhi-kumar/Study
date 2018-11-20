# R-CNN

[Source 1](https://lilianweng.github.io/lil-log/2017/12/31/object-recognition-for-dummies-part-3.html#r-cnn), [Source 2](https://www.learnopencv.com/selective-search-for-object-detection-cpp-python/), 

## 1. Introduction

### 1.1. What is RCNN
- Is short for “Region-based Convolutional Neural Networks”.
- It involved two steps:
  - using selective search, it identifies a manageable number of bounding-box object region candidates (“region of interest” or “RoI”). 
  - then it extracts CNN features from each region independently for classification.
  
  
### 1.2. How does selective search work
- It is a region proposal algorithm used in object detection.
- Starts by over-segmenting the image based on intensity of the pixels using a graph-based segmentation method by Felzenszwalb and Huttenlocher. 
- Bounding box iteration:
  - Add all bounding boxes corresponding to segmented parts to the list of regional proposals
  - Group adjacent segments based on similarity
  - Iterate over again till stopping criteria reached.
- Larger segments are formed and added to the list of region proposals. Hence we create region proposals from smaller segments to larger segments in a bottom-up approach. This is what we mean by computing “hierarchical” segmentations using Felzenszwalb and Huttenlocher’s oversegments.


## 5. Examples
  
### 5.1. Automated simple faster RCNN
  - It is a code that uses [pypi based selectivesearch](https://pypi.org/project/selectivesearch/)
  - Image loading is done using OpenCV
  - In the example, the output has a few (not all) bounding boxex for better visualization.
  - The implementation is quite slow.
  - Intallation: 
    - pip install numpy opencv-python selectivesearch
  - Running the code:
    - python selective_search_auto.py
  
 
