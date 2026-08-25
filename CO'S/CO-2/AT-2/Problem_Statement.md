# CO-2 AT-2 – Scenario-Based Assessment: Activation Functions

## Problem Statement

A college wants to develop a **Deep Learning model** to classify students into two categories: **Pass** and **Fail** based on their academic performance.

The model uses the following three input features:

- Internal Marks
- Attendance
- Assignment Marks

The proposed neural network consists of:

- **Input Layer:** 3 neurons
- **Hidden Layer:** 4 neurons
- **Output Layer:** 1 neuron

During model development and testing, different activation functions are evaluated. When **Sigmoid** is used in the hidden layer, the network learns very slowly due to the vanishing gradient problem. When **ReLU** is used, some neurons continuously produce an output of zero, causing them to stop learning. At the same time, the output layer must produce a value between **0 and 1** so that the result can be interpreted as the probability of a student passing.

Therefore, an appropriate activation function must be selected for both the hidden and output layers. The behavior and limitations of **Sigmoid, ReLU, and Leaky ReLU** must also be analysed mathematically.

## Tasks

The assessment requires the following:

### A. Output Layer Activation

Identify the most suitable activation function for the output layer and explain why it is appropriate for binary classification.

### B. Hidden Layer Activation

Identify a suitable activation function for the hidden layer that can overcome the slow-learning problem associated with Sigmoid.

### C. Dying ReLU Problem

Identify and explain the problem that occurs when ReLU neurons continuously produce an output of zero.

### D. Alternative Activation Function

Suggest an activation function that can overcome the dying ReLU problem and explain how it works.

### E. Mathematical Calculation

For the given neuron input, calculate the output using:

1. ReLU
2. Leaky ReLU
3. Sigmoid

Show the mathematical calculations and intermediate steps clearly.

### F. Comparative Analysis

Compare ReLU and Leaky ReLU for negative input values and explain why Leaky ReLU can be more useful when ReLU neurons become inactive.

## Expected Learning Outcomes

After completing this assessment, the student should be able to:

- Select appropriate activation functions based on a classification problem.
- Explain the purpose of activation functions in neural networks.
- Calculate outputs of ReLU, Leaky ReLU, and Sigmoid.
- Identify the **vanishing gradient problem** associated with Sigmoid.
- Identify the **dying ReLU problem**.
- Explain how Leaky ReLU helps overcome dying neurons.
- Justify the use of Sigmoid in binary classification output layers.
- Compare different activation functions based on their properties and applications.
- Apply activation-function concepts to a real-world student Pass/Fail prediction problem.

## Neural Network Architecture

```text
             INPUT LAYER
          ┌─────────────────┐
          │ Internal Marks  │
          │ Attendance      │
          │ Assignment      │
          │ Marks            │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │  HIDDEN LAYER   │
          │   4 Neurons     │
          │ ReLU / Leaky    │
          │      ReLU       │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │  OUTPUT LAYER   │
          │    1 Neuron     │
          │    Sigmoid      │
          └────────┬────────┘
                   │
                   ▼
          ┌─────────────────┐
          │ Pass Probability│
          │      0–1        │
          └────────┬────────┘
                   │
             ┌─────┴─────┐
             ▼           ▼
           PASS         FAIL
