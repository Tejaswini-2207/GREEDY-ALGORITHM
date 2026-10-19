#Scenario: An exam hall must be used for the maximum number of exams. Each exam has a start and finish time.


def exam_scheduling(exams):
    exams = sorted(exams, key=lambda x: x[1])
    selected = []
    last_finish = float("-inf")

    for start, finish in exams:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish

    return selected


exams = [
    (3, 4), (1, 2), (0, 6),
    (5, 7), (8, 9), (5, 9), (2, 4)
]

result = exam_scheduling(exams)
print("Selected exams:", result)
print("Maximum exams:", len(result))
