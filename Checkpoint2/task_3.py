def process_intervals(intervals: list[list[int]]) -> list[list[int]] | None:
    if not intervals:
        return

    intervals.sort()
    result = [intervals[0]]
    for interval in intervals[1:]:
        start = interval[0]
        end = interval[1]

        last_element = result[-1][1]
        if start <= last_element:
            result[-1][1] = max(last_element, end)
        else:
            result.append([start, end])
    return result

intervals = [[1, 3],[2, 6],[8, 10],[10, 12]]
print(process_intervals(intervals))
