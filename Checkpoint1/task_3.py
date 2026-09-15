def max_items(nums: list[int]) -> int:
    if not nums:
        return 0
    left = 0
    max_count = 0
    count = {}
    for right, current_item in enumerate(nums):
        count[current_item] = count.get(current_item, 0) + 1
        while len(count) > 2:
            left_item = nums[left]
            count[left_item] -= 1
            if count[left_item] == 0:
                del count[left_item]
            left += 1
        window = right - left + 1
        max_count = max(max_count, window)
    return max_count

numbers = [1, 2, 3, 2, 2]
print(max_items(numbers))
