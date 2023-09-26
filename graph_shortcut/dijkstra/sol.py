import heapq

def dijkstra():
    distances = [[float('inf') for _ in range(max(price)+1)] for _ in range(N+1)]
    heap = [(0,price[1],1)]
    distances[1][price[1]] = 0
    while heap:
        now_weight, now_price, now = heapq.heappop(heap)
        if now == N:
            return now_weight
        if now_weight <= distances[now][now_price]:
            for next, weight in graph[now]:
                next_price = min(now_price, price[next])
                next_weight = now_weight + (weight * now_price)
                if distances[next][now_price] > next_weight:
                    distances[next][now_price] = next_weight
                    heapq.heappush(heap, (next_weight, next_price, next))

N, M = map(int, input().split())
price = [0] + list(map(int, input().split()))
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b, w = map(int, input().split())
    graph[a].append((b,w))
    graph[b].append((a,w))
print(dijkstra())