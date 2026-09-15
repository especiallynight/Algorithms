def max_area(height):
    left = 0
    right = len(height) - 1
    answer = 0

    while left < right:
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height

        answer = max(answer, current_area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return answer
numbers = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(numbers))