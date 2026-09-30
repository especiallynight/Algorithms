def FindTheNearestPrice(prices: list[int]) -> list[int]:
    answer = [0] * len(prices)
    stack = []
    for i, price in enumerate(prices):
        while stack and price > prices[stack[-1]]:
            j = stack.pop()
            answer[j] = i - j

        stack.append(i)

    return answer
prices = [5, 1, 6, 7, 2, 4]
print(FindTheNearestPrice(prices))