def findMinRooms(meetings: list[list[int]]) -> int:
    events = []

    for start, end in meetings:
        events.append((start, 1))
        events.append((end, -1))

    events.sort(key=lambda event: (event[0], event[1]))

    rooms = 0
    max_rooms = 0
    for _, change in events:
        rooms += change
        max_rooms = max(max_rooms, rooms)

    return max_rooms

meetings = [[1, 3], [2, 6], [8, 10], [10, 12]]
print(findMinRooms(meetings))