# CO4 – AT1 – Design and Develop Model

## SAVEETHA SCHOOL OF ENGINEERING (SIMATS)

### DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING

---

## Assessment Information

| Field | Details |
|---|---|
| **Course Code** | MLA04 |
| **Course Title** | Deep Learning |
| **Course Outcome** | CO4 |
| **Assessment Tool** | CO4-AT1 – Design and Develop Model |
| **Weightage** | 20% |
| **Total Marks** | 25 |
| **Duration** | 60 Minutes |

---

## Student Details

- **Student Name:** Paleru Dharani Govardhan
- **Register Number:** 192525280
- **Department:** Artificial Intelligence and Machine Learning
- **Course:** Deep Learning
- **Date:** __________
- **Signature:** __________

---

## CO4 Statement

> Analyze linear factor models and structured probabilistic models using graphical modelling and feature analysis techniques.

---

# Problem Statement

## Design and Develop an LSTM-Based Deep Learning Model for Student Performance Prediction

A university wants to develop a **Deep Learning-based student performance prediction system** that can predict a student's performance in the next semester using their previous semester marks.

Student academic performance is sequential in nature because a student's current performance may be related to their performance in previous semesters. Therefore, the university wants to develop an **LSTM (Long Short-Term Memory) model** capable of learning sequential relationships from historical semester marks and predicting future academic performance.

The university has collected the following sample data:

| Student | Semester 1 | Semester 2 | Semester 3 | Semester 4 |
|---|---:|---:|---:|---:|
| S1 | 56 | 45 | 55 | 60 |
| S2 | 70 | 68 | 72 | 75 |
| S3 | 40 | 48 | 45 | 50 |
| S4 | 85 | 82 | 88 | 90 |
| S5 | 60 | 55 | 58 | 62 |

The objective is to **design and develop an LSTM-based Deep Learning model** that learns the sequential relationship between semester marks and predicts the student's performance in the next semester.

The overall system can be represented as:

```text
Previous Semester Marks
          ↓
    Data Preparation
          ↓
      Normalization
          ↓
   Sequence Formation
          ↓
      LSTM Network
          ↓
   Learned Sequence Pattern
          ↓
 Next Semester Prediction
          ↓
 Actual vs Predicted
          ↓
    Model Evaluation
