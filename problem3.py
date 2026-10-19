#Problem 1: College Seminar Scheduling (Easy)
#Scenario: A student wants to attend the maximum number of seminars without overlapping.


def activity_selection(activities):
    activities = sorted(activities, key=lambda x: x[1])
    selected = []
    last_finish = float("-inf")

    for start, finish in activities:
        if start >= last_finish:
            selected.append((start, finish))
            last_finish = finish

    return selected


activities = [(1, 3), (2, 5), (4, 6), (6, 8)]
result = activity_selection(activities)

print("Selected activities:", result)
print("Maximum count:", len(result))
