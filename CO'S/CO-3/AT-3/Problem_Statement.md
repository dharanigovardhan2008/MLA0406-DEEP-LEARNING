# CO3 – AT3 – Comparative Analysis Task

## Problem Statement

A university wants to develop an **image classification system for identifying different types of plant diseases from leaf images** using **Convolutional Neural Networks (CNNs)**.

The available dataset is relatively small, and the leaf images contain significant variations in:

- Lighting conditions
- Leaf orientation
- Image backgrounds
- Scale and position of leaves
- Visual appearance of disease symptoms

These variations create challenges in extracting useful features and building a CNN model that can **generalize well to unseen images**.

To develop an effective solution, different **convolution operations, filters, regularization techniques, and CNN architectures** must be analysed and compared.

The study focuses on understanding how different convolution operations affect feature extraction, spatial dimensions, and computational complexity. It also evaluates how regularization techniques can reduce overfitting, particularly when training CNNs on a relatively small dataset.

Furthermore, the study compares four popular CNN architectures:

- **AlexNet**
- **VGGNet**
- **ResNet**
- **DenseNet**

The architectures are evaluated based on their design, number of layers, parameter size, computational requirements, feature reuse, gradient flow, advantages, limitations, and suitability for plant disease classification.

## Tasks

### Part A – Convolution Operations and Filters

Analyse at least four convolution operations or filters, such as:

- Standard Convolution
- Strided Convolution
- Dilated/Atrous Convolution
- Depthwise Convolution
- Pointwise Convolution
- Separable Convolution
- Max Pooling
- Average Pooling

For each selected operation, analyse:

- Working principle
- Kernel/filter characteristics
- Effect on feature extraction
- Effect on spatial dimensions
- Computational complexity
- Advantages
- Limitations
- Suitable application scenarios

Include appropriate diagrams, calculations, or examples.

### Part B – Regularization Techniques

Compare at least three regularization techniques, such as:

- Dropout
- L1/L2 Regularization
- Data Augmentation
- Batch Normalization
- Early Stopping

For each technique, analyse:

- Purpose
- How it reduces overfitting
- Effect on training and validation performance
- Advantages
- Limitations
- Suitable CNN applications

Also explain the difference between:

- Underfitting
- Good Generalization
- Overfitting

using suitable training and validation examples.

### Part C – CNN Architecture Comparison

Compare the following CNN architectures:

- AlexNet
- VGGNet
- ResNet
- DenseNet

The comparison should consider:

- Year introduced
- Basic architecture
- Number of layers
- Convolutional filters
- Key innovation
- Parameter size
- Computational requirements
- Handling of vanishing/degradation problems
- Feature reuse
- Advantages
- Limitations
- Typical applications

### Part D – Scenario-Based Analysis

For the plant disease classification problem:

1. Select a suitable convolution operation/filter and justify the choice.
2. Identify appropriate regularization techniques and explain why they are required.
3. Select the most appropriate CNN architecture from AlexNet, VGGNet, ResNet, and DenseNet.
4. Compare the selected architecture with at least two alternative architectures.
5. Explain how the proposed combination can improve classification accuracy and generalization.
6. Identify at least two challenges and propose suitable solutions.

### Part E – Critical Analysis

Answer the following questions:

1. Why does increasing the number of convolutional layers not always improve CNN performance?
2. How do different filter sizes affect feature extraction and computational cost?
3. Why are depthwise separable convolutions computationally efficient?
4. Why is regularization particularly important when training CNNs on small datasets?
5. How does ResNet overcome the degradation problem in deep networks?
6. How does DenseNet promote feature reuse?
7. Which CNN architecture would you recommend for the plant-disease classification problem? Justify your answer based on accuracy, computational cost, dataset size, and generalization.

## Expected Learning Outcomes

After completing this assessment, the student should be able to:

- Analyse different convolution operations and filters.
- Explain how CNN filters extract visual features.
- Calculate and compare convolutional computational requirements.
- Analyse the effect of stride, padding, and dilation on feature maps.
- Explain the purpose of regularization in CNNs.
- Identify and distinguish underfitting, overfitting, and good generalization.
- Compare AlexNet, VGGNet, ResNet, and DenseNet.
- Analyse the advantages and limitations of different CNN architectures.
- Select suitable CNN components for a real-world image classification problem.
- Justify architecture and regularization choices based on dataset characteristics.
- Evaluate trade-offs between accuracy, computational cost, feature reuse, and generalization.

## Scenario

```text
                PLANT LEAF IMAGE
                       │
                       ▼
              ┌─────────────────┐
              │  PREPROCESSING   │
              │ Resize / Normalize│
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ DATA AUGMENTATION│
              │ Rotation / Flip  │
              │ Lighting / Crop  │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │      CNN        │
              │ Feature Extraction│
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Regularization  │
              │ Dropout / L2    │
              └────────┬────────┘
                       │
                       ▼
              ┌─────────────────┐
              │ Classification  │
              └────────┬────────┘
                       │
                       ▼
          ┌────────────┴────────────┐
          │                         │
          ▼                         ▼
     Healthy Leaf            Diseased Leaf
                              │
                       Disease Category
