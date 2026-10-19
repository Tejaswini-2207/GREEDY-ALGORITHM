#Scenario: A company has one conference room and several meeting requests. Each request has a start time and finish time. Return the maximum number of meetings that can be conducted.


def conference_scheduling(meetings):
    meetings = sorted(meetings, key=lambda x: x[1])
    selected = []
    last_finish = float("-inf")

    for start, finish in meetings:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish

    return selected


meetings = [
    (7, 9), (0, 10), (3, 4), (1, 2),
    (5, 7), (8, 9), (2, 5), (9, 11)
]

result = conference_scheduling(meetings)
print("Selected meetings:", result)
print("Maximum meetings:", len(result))
