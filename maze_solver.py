import collections
import time
import heapq


def solve_maze_bfs(maze, start, end):
    """Resuelve el laberinto usando BFS."""
    rows, cols = len(maze), len(maze[0])
    queue = collections.deque([(start, [start])])
    visited = set([start])

    start_time = time.time()

    while queue:
        (r, c), path = queue.popleft()

        if (r, c) == end:
            return path, time.time() - start_time

        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and \
               maze[nr][nc] == 0 and (nr, nc) not in visited:

                visited.add((nr, nc))
                queue.append(((nr, nc), path + [(nr, nc)]))

    return None, time.time() - start_time



# -------------------------
# DFS (AGREGADO)
# -------------------------
def solve_maze_dfs(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    stack = [(start, [start])]
    visited = set([start])

    start_time = time.time()

    while stack:
        (r, c), path = stack.pop()

        if (r, c) == end:
            return path, time.time() - start_time

        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and \
               maze[nr][nc] == 0 and (nr, nc) not in visited:

                visited.add((nr, nc))
                stack.append(((nr, nc), path + [(nr, nc)]))

    return None, time.time() - start_time



# -------------------------
# A* (AGREGADO)
# -------------------------
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def solve_maze_astar(maze, start, end):
    rows, cols = len(maze), len(maze[0])
    start_time = time.time()

    pq = [(0, start, [start])]
    visited = set()

    while pq:
        f, (r, c), path = heapq.heappop(pq)

        if (r, c) == end:
            return path, time.time() - start_time

        if (r, c) in visited:
            continue
        visited.add((r, c))

        for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols and maze[nr][nc] == 0:
                g = len(path) + 1
                h = heuristic((nr, nc), end)
                heapq.heappush(pq, (g + h, (nr, nc), path + [(nr, nc)]))

    return None, time.time() - start_time



# -------------------------
# Laberinto y posiciones
# -------------------------
MAZE = [
[10111111111111111111111111111111],
[10100010001000000000100000000011],
[10101010101111101110111011111011],
[10001000101000001010000010001001],
[11111111101011111011111110101111],
[10000000101000001000001000100011],
[11101111101011101011101111101011],
[10001000001010001010001000001011],
[10111011111110111010111011111111],
[10100010001000100010001010000001],
[10101110101011101111101010111111],
[10101000100010001000101010001011],
[10101010111110101011101011101011],
[10001010100010101000000010001001],
[10111110101010101011111110111111],
[10000010101010101000100010000011],
[11111010101010101110101011111011],
[10000010001010101000101000001011],
[10111110111010101111101110101011],
[10001000100010100000000010101011],
[11101111101111101111111110101011],
[10101000001000101000100000101011],
[10101011111010101010101111111011],
[10101000100010101010001000000011],
[10101110101110111010111011111111],
[10001000101010001010100010000011],
[10111011101011101011101110111011],
[10001000001000101000001000100011],
[11101110111011101011111010111011],
[10100010000010001010000010001001],
[10111010111110111010111111101111],
[10100010100000101010100010001011],
[10101111101111101010101010111011],
[10100000101000001010101000101001],
[10111110101010111011101111101011],
[10000000001010000000001000000001],
[11111111111111111111111111111101]
]

START = (0, 1)
END = (36, 30)
