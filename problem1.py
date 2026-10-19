#Scenario: A hospital has several appointments. Each appointment has a start time and finish time. The hospital wants to schedule the maximum number of non-overlapping appointments in one room.


def activity_selection(appointments):
    appointments = sorted(appointments, key=lambda x: x[1])

    selected = []
    last_finish = float("-inf")

    for start, finish in appointments:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish

    return selected


appointments = [
    (1, 4), (3, 5), (0, 6),
    (5, 7), (8, 9), (5, 9)
]

result = activity_selection(appointments)

print("Selected appointments:", result)
print("Maximum appointments:", len(result))
