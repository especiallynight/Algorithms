def min_capacity(weights: list[int], days: int) -> int:
    left = max(weights)
    right = sum(weights)

    while left < right:
        capacity = (left + right) // 2
        current_weight = 0
        days_needed = 1

        for weight in weights:
            if current_weight + weight > capacity:
                days_needed += 1
                current_weight = 0

            current_weight += weight

        if days_needed <= days:
            right = capacity
        else:
            left = capacity + 1
    return left

weights = [3, 2, 2, 4, 1, 4]
days = 3
print(min_capacity(weights, days))