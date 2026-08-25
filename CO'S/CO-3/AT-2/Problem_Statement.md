# CO3 – AT2 – Game-Based Learning Analysis

## SAVEETHA SCHOOL OF ENGINEERING (SIMATS)

### DEPARTMENT OF COMPUTER SCIENCE AND ENGINEERING

---

## Assessment Information

| Field | Details |
|---|---|
| **Course Code** | MLA04 |
| **Course Title** | Deep Learning |
| **Course Outcome** | CO3 |
| **Assessment Tool** | AT2 – Game-Based Learning Analysis |
| **Assessment Type** | Case Study / Game-Based Learning Analysis |
| **Weightage** | 20% |
| **Total Marks** | 25 |
| **Duration** | 60 Minutes |

---

# Problem Statement

## Designing a Game-Based Learning System Using Deep Learning

A university wants to develop an **interactive game-based learning system** to improve students' understanding, engagement, motivation, and learning outcomes.

Traditional teaching methods may not always maintain students' interest or provide personalized learning experiences. A fixed learning approach may also fail to adapt to differences in students' knowledge levels, learning speed, performance, and engagement.

The proposed system should use game elements such as:

- Levels
- Challenges
- Scores
- Rewards
- Feedback
- Hints
- Progress tracking
- Adaptive difficulty

Deep Learning techniques should be incorporated to analyse student interactions, identify performance patterns, predict learning performance, and provide personalized challenges based on each student's progress.

The system should continuously observe student behaviour and use the collected information to determine the most appropriate next action.

For example:

- A student performing consistently well may receive a more difficult challenge.
- A student struggling with a topic may receive an easier challenge.
- A student repeatedly making the same mistake may receive a hint or targeted practice.
- A student showing improvement may gradually move to a higher difficulty level.

The proposed system can model the learning process as a sequential decision-making problem:

```text
┌──────────────────────┐
│    Student State     │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Deep Learning Agent  │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Action / Challenge   │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Student Response     │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Reward / Feedback    │
└──────────┬───────────┘
           ↓
┌──────────────────────┐
│ Updated Student State│
└──────────┴───────────┘
           ↺
