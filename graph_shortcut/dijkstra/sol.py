import heapq
from pprint import pprint

delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dijkstra(i, j):
    visited = [[float('inf') for _ in range(w+2)] for _ in range(h+2)]
    heap = [(0, i, j)]
    visited[i][j] = 0
    while heap:
        weight, x, y = heapq.heappop(heap)
        if visited[x][y] >= weight:
            for d in range(4):
                nx = x + delta[d][0]
                ny = y + delta[d][1]
                if 0 <= nx < h and 0 <= ny < w and graph[nx][ny] != '*' and visited[nx][ny] > weight:
                    if graph[nx][ny] == '#':
                        visited[nx][ny] = weight + 1
                        heapq.heappush(heap, (weight + 1, nx, ny))
                    else:
                        visited[nx][ny] = weight
                        heapq.heappush(heap, (weight, nx, ny))
    return visited

T = int(input())
for t in range(T):
    h, w = map(int, input().split())
    graph = [['.' for _ in range(w+2)]]
    start_point = []
    for i in range(1, h+1):
        graph.append(['.'] + list(input()) + ['.'])
        for j in range(w+2):
            if graph[i][j] == '$':
                start_point.append((i, j))
    graph.append(['.' for _ in range(w+2)])
    min_steps = float('inf')
    steps1 = dijkstra(start_point[0][0], start_point[0][1])
    steps2 = dijkstra(start_point[1][0], start_point[1][1])
    outer = dijkstra(0, 0)
    for i in range(h+2):
        for j in range(w+2):
            if graph[i][j] != "*":
                total_steps = steps1[i][j] + steps2[i][j] + outer[i][j]
                if graph[i][j] == "#":
                    total_steps -= 2
                min_steps = min(min_steps, total_steps)
    print(min_steps)
