from queue import Queue


def shortest_path(matrix, start, end):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    rows, cols = len(matrix), len(matrix[0])
    visited = set()
    q = Queue()
    q.put((start, 0))
    visited.add(start)

    while not q.empty():
        (x, y), dist = q.get()

        if (x, y) == end:
            return dist

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < rows and 0 <= new_y < cols and (new_x, new_y) not in visited and matrix[new_x][new_y] == 1:
                q.put(((new_x, new_y), dist + 1))
                visited.add((new_x, new_y))

    return -1


with open('input.txt', 'r') as file:
    start = tuple(map(int, file.readline().strip().split(', ')))
    end = tuple(map(int, file.readline().strip().split(', ')))
    rows, cols = map(int, file.readline().strip().split(','))
    matrix = []
    for _ in range(rows):
        row = list(map(int, file.readline().strip()[1:-1].split()))
        matrix.append(row)

shortest_dist = shortest_path(matrix, start, end)

with open('output.txt', 'w') as file:
    file.write(str(shortest_dist))
