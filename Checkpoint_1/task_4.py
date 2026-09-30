def sumOfSubarrays(nums: list[int], k: int) -> int:
    prefix_counts = {0:1}
    current_sum = 0
    total_subarrays = 0
    for num in nums:
        current_sum += num
        needed_sum = current_sum - k
        if needed_sum in prefix_counts:
            total_subarrays += prefix_counts[needed_sum]
        prefix_counts[current_sum] = prefix_counts.get(current_sum,0)+1
    return total_subarrays
numbers = [1, -1, 0]
print(sumOfSubarrays(numbers,0))
