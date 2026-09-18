def subarraySum(nums,k):
    prefix_sum = {0: 1}
    current_sum = 0
    counter = 0

    for num in nums:
        current_sum += num
        needed = current_sum - k

        if needed in prefix_sum:
            counter += prefix_sum[needed]
        prefix_sum[current_sum] = prefix_sum.get(current_sum, 0) + 1

    return counter
nums = [1, 2, 3, 1, -5, 7, 1]
print(subarraySum(nums, 3))