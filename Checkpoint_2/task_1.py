def insertTarget(nums,target):
    left = 0
    right = len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid
    return left
nums = [1, 2, 3, 4, 6]
target = 5
print(insertTarget(nums,target))