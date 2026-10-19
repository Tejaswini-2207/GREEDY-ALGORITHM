#Scenario: A research laboratory receives these experiment requests. The lab has one machine, so experiments cannot overlap. Design a greedy algorithm to maximize the number of experiments completed.


def max_experiments(experiments):
    experiments = sorted(experiments, key=lambda x: x[1])
    selected = []
    last_finish = float("-inf")

    for name, start, finish in experiments:
        if start >= last_finish:
            selected.append(name)
            last_finish = finish

    return selected


experiments = [
    ("E1", 1, 4),
    ("E2", 3, 5),
    ("E3", 0, 6),
    ("E4", 5, 7),
    ("E5", 8, 9),
    ("E6", 5, 9),
    ("E7", 9, 11)
]

result = max_experiments(experiments)
print("Selected experiments:", result)
print("Maximum experiments:", len(result))
