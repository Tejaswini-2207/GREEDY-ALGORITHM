#Scenario: A delivery company has a truck with a maximum capacity of 50 kg. Each product has a weight and profit. Products can be divided, and the goal is to maximize the profit loaded onto the truck.


def fractional_knapsack(items, capacity):
    # Each item: (name, weight, profit)
    items = sorted(
        items,
        key=lambda item: item[2] / item[1],
        reverse=True
    )

    total_profit = 0.0
    selected = []

    for name, weight, profit in items:
        if capacity <= 0:
            break

        if weight <= capacity:
            selected.append((name, 1.0))
            total_profit += profit
            capacity -= weight
        else:
            fraction = capacity / weight
            selected.append((name, fraction))
            total_profit += profit * fraction
            capacity = 0

    return selected, total_profit


items = [
    ("A", 10, 60),
    ("B", 20, 100),
    ("C", 30, 120)
]

selected, profit = fractional_knapsack(items, 50)

print("Selected products:", selected)
print("Maximum profit:", round(profit, 2))
