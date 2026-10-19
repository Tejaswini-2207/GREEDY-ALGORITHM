# Greedy Algorithm: Activity Selection Problems

## 📌 Overview

This repository contains five scenario-based implementations of the **Activity Selection Problem** using the Greedy Algorithm in Python.

The objective is to select the maximum number of non-overlapping activities from a given set of activities, assuming only one activity can be performed at a time.

## 🎯 Objectives

- Understand the Greedy Algorithm approach.
- Implement Activity Selection using Python.
- Solve real-world scheduling problems.
- Learn pseudocode, algorithm design, and complexity analysis.
- Practise scenario-based questions for Advanced Algorithm Design.

## 🧠 Greedy Strategy

The algorithm follows these steps:

1. Sort all activities by their finishing time in ascending order.
2. Select the activity that finishes earliest.
3. Examine the remaining activities one by one.
4. Select an activity if its start time is greater than or equal to the finish time of the last selected activity.
5. Return the selected activities.

**Key idea:** Choosing the earliest finishing compatible activity leaves as much time as possible for subsequent activities.

## 📝 General Pseudocode

```text
ACTIVITY-SELECTION(activities):
    sort activities by finish time
    selected = empty list
    last_finish = -infinity

    for each activity (start, finish):
        if start >= last_finish:
            add activity to selected
            last_finish = finish

    return selected
```

## 💻 Problems Implemented

### Problem 1: College Seminar Scheduling

**Scenario:** Select the maximum number of non-overlapping seminars that a student can attend.

**Input:**
```python
activities = [(1, 3), (2, 5), (4, 6), (6, 8)]
```

**Output:**
```text
Selected activities: [(1, 3), (4, 6), (6, 8)]
Maximum count: 3
```

### Problem 2: Hospital Appointment Scheduling

**Scenario:** Schedule the maximum number of patients in a single doctor's room without overlapping appointments.

**Input:**
```python
appointments = [
    (1, 4), (3, 5), (0, 6), (5, 7), (8, 9)
]
```

**Output:**
```text
Selected appointments: [(1, 4), (5, 7), (8, 9)]
Maximum patients: 3
```

### Problem 3: University Exam Hall Scheduling

**Scenario:** Select the maximum number of exams that can be conducted in a single exam hall without time conflicts.

**Input:**
```python
exams = [
    (3, 4), (1, 2), (0, 6),
    (5, 7), (8, 9), (5, 9), (2, 4)
]
```

**Output:**
```text
Selected exams: [(1, 2), (2, 4), (5, 7), (8, 9)]
Maximum exams: 4
```

### Problem 4: Conference Room Scheduling

**Scenario:** Select the maximum number of meetings that can be conducted in one conference room.

**Input:**
```python
meetings = [
    (7, 9), (0, 10), (3, 4), (1, 2),
    (5, 7), (8, 9), (2, 5), (9, 11)
]
```

**Output:**
```text
Selected meetings: [(1, 2), (3, 4), (5, 7), (7, 9), (9, 11)]
Maximum meetings: 5
```

### Problem 5: Research Laboratory Experiment Scheduling

**Scenario:** Select the maximum number of experiments that can run on a single machine without overlapping.

**Input:**
```python
experiments = [
    ("E1", 1, 4),
    ("E2", 3, 5),
    ("E3", 0, 6),
    ("E4", 5, 7),
    ("E5", 8, 9),
    ("E6", 5, 9),
    ("E7", 9, 11)
]
```

**Output:**
```text
Selected experiments: ['E1', 'E4', 'E5', 'E7']
Maximum experiments: 4
```

## ⏱️ Complexity Analysis

Let `n` be the number of activities.

| Operation | Time Complexity |
|---|---|
| Sorting activities | O(n log n) |
| Selecting compatible activities | O(n) |
| Overall time complexity | **O(n log n)** |
| Auxiliary space | O(n) for the sorted copy and selected list |

## 🛠️ Technologies Used

- **Programming Language:** Python 3
- **Algorithm Technique:** Greedy Algorithm
- **Concepts:** Sorting, Lists, Iteration, Conditional Statements
- **Development Environment:** VS Code / GitHub Codespaces

## ▶️ How to Run

1. Clone or open the repository in GitHub Codespaces.
2. Open the Python file containing the desired problem.
3. Run the program in the terminal:

```bash
python activity_selection.py
```

Replace `activity_selection.py` with the actual filename of the Python file you want to execute.

## 📚 Key Learnings

- How greedy algorithms make locally optimal choices.
- How sorting by finishing time helps maximize compatible activities.
- How to translate pseudocode into Python.
- How to apply one algorithm to different real-world scenarios.
- How to analyse time and space complexity.

## ⚠️ Important Note

The five problems in this repository are different applications of the same classic Activity Selection algorithm. The greedy approach is optimal for maximizing the number of mutually compatible activities when activities have fixed start and finish times and one resource is available.

## 👩‍💻 Author

Created as part of Advanced Algorithm Design practice to strengthen greedy algorithm implementation and scenario-based problem-solving skills.

---

**Topics:** `Greedy Algorithm` `Activity Selection` `Python` `Algorithm Design` `Pseudocode` `Time Complexity` `Scheduling Problems`
