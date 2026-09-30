def process_queries(nums, queries):
    pref = [0] * (len(nums) + 1)
    for i in range(len(nums)):
        pref[i + 1] = pref[i] + nums[i]

    result = []
    for L, R in queries:
        result.append(pref[R + 1] - pref[L])
    return result
nums = [1, 2, 3, 4, 5]
queries = [(0, 2), (1, 3), (2, 4)]

print(process_queries(nums, queries))
