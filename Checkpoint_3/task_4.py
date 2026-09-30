matrix = [
    "1011",
    "1111",
    "0111",
]

n = len(matrix)
m = len(matrix[0])

heights = [0] * m
answer = 0

for row in matrix:
    for j in range(m):
        heights[j] = heights[j] + 1 if row[j] == "1" else 0

    stack = []

    for j in range(m + 1):
        current = heights[j] if j < m else 0

        while stack and heights[stack[-1]] > current:
            height = heights[stack.pop()]
            left = stack[-1] + 1 if stack else 0
            width = j - left
            answer = max(answer, height * width)

        stack.append(j)

print(answer)
