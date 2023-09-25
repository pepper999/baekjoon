import heapq

def dijkstra(i, j):
    visited = [[0 for _ in range(w)] for _ in range(h)]
    heap = [(0,i,j)]
    visited[i][j] = 1
    while heap:
        


T = int(input())
for t in range(T):
    h, w = map(int, input().split())
    graph = []
    break_spot = []
    for i in range(h):
        graph.append(list(input()))
        if i == 0 or i == h-1:
            for j in range(w):
                if graph[i][j] == '#':
                    break_spot.append([i,j,1])
                elif graph[i][j] == '.':
                    break_spot.append([i,j,0])
        else:
            if graph[0] == '#':
                break_spot.append([i,0,1])
            elif graph[0] == '.':
                break_spot.append([i,0,0])
            elif graph[-1] == '#':
                break_spot.append([i,w-1,1])
            elif graph[-1] == '.':
                break_spot.append([i,w-1,0])
    print(break_spot)