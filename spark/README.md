# Spark and Machine learning

[Source 1](https://towardsdatascience.com/deep-learning-with-apache-spark-part-1-6d397c16abd), 


## 1. Introduction

### 1.1. What is Apache Spark?
  - a fast and general engine for large-scale data processing.
  - runs on Memory (RAM), and that makes the processing much faster than on Disk.
  
### 1.2. What is RDD?
  - Resilient Distributed Dataset.
  - a fault-tolerant collection of elements that can be operated on in parallel.
  
### 1.3. What is spark's Catalyst?
  - A library for optimization
  - will take the queries and the actions and create an optimized plan for distributing the computation.
  
  
  
## 2. Elephas + Keras

### 2.1 What is Elephas?
  - is an extension of Keras
  - run distributed deep learning models at scale with Spark.
  - allowing for fast prototyping of distributed models
  - implements a class of data-parallel algorithms on top of Keras
  - uses Spark's RDDs and data frames.

### 2.2 Elements in Elephas?
  - basic model in Elephas is the SparkModel
    - initialize a SparkModel by passing in a compiled Keras model
  - Elephas fit has the same options as a Keras model, so you can pass epochs, batch_size etc, same as in Keras.


