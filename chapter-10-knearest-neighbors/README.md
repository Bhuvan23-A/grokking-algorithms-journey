# Chapter 10: K-Nearest Neighbors (KNN)

This chapter introduces the **k-nearest neighbors (KNN)** algorithm, a
simple yet powerful machine learning technique used for classification
and prediction.

## Classification and Feature Extraction

To apply KNN, items must be converted into **feature vectors**—lists of
numbers that represent measurable properties.

- **Graphing Data**  
  You cannot plot a concept like “fruit” directly. Instead, you might
  measure attributes such as **size** and **color intensity** and plot
  those values in coordinate space.

- **The Algorithm**  
  To classify a new item, KNN looks at its **k nearest neighbors** in
  feature space. If most of the neighbors are oranges, the mystery fruit
  is classified as an orange.

## The Mathematics of Similarity

KNN determines similarity based on distance between feature vectors.

- **Euclidean Distance**  
  The standard measure uses the Pythagorean formula:

  \[
  d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}
  \]

  This generalizes easily to higher dimensions (more features).

- **Cosine Similarity**  
  Euclidean distance can fail when users rate items on different scales
  (e.g., harsh vs generous raters). In such cases, **cosine similarity**
  compares the **angle** between vectors rather than their magnitude,
  making it useful for recommendation systems.

## Two Modes of KNN

KNN can be used in two different ways:

1. **Classification**  
   Assigning data to categories  
   (e.g., “Does this person like sci-fi?”)

2. **Regression**  
   Predicting numerical values  
   (e.g., “What rating will this user give a movie?”)

## Introduction to Machine Learning

KNN is introduced as a gentle entry point into **machine learning**,
illustrating how data-driven algorithms can make decisions without
explicit rules.

Examples:

- **Recommendation Systems**  
  Netflix compares user taste vectors. If user A and user B have similar
  preferences, movies enjoyed by B are recommended to A.

- **OCR (Optical Character Recognition)**  
  Characters are converted into feature vectors of curves and shapes,
  and then matched against known labeled examples.

- **Spam Filtering**  
  While KNN can classify emails, **Naive Bayes** is more commonly used
  for spam detection.

## Practical Considerations

Because KNN uses distance, features must be:

- **Scaled** to similar ranges (so one feature doesn't dominate)
- **Numerical**, which is why feature extraction is necessary

KNN also becomes expensive with large datasets since it must compare the
new sample to many existing samples.

## Intuition

Classifying a mystery fruit using KNN is like **guessing a stranger’s
personality by looking at their three best friends**. If the stranger’s
closest friends are loud, extroverted comedians, it is statistically
likely the stranger is also an extrovert. KNN classifies items based on
the characteristics of their nearest neighbors.

## Code

Examples of KNN classification and regression are provided in
`chapter_10_knearest_neighbors.py`.

