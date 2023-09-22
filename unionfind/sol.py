import sys
sys.setrecursionlimit(int(1e6))
def sol():
    def find_parents(a):
        if parents[a] != a:
            parents[a] = find_parents(parents[a])
        return parents[a]

    def union(a, b):
        a = find_parents(a)
        b = find_parents(b)
        if a < b:
            parents[b] = a
        else:
            parents[a] = b

    N = int(input())
    M = int(input())
    parents = [i for i in range(N+1)]
    for i in range(1, N+1):
        edge = list(map(int, input().split()))
        for j in range(1, N+1):
            if edge[j-1] == 1:
                union(i, j)
    plans = list(map(int, input().split()))
    for i in range(M-1):
        if find_parents(plans[i]) != find_parents(plans[i+1]):
            print('NO')
            return
    print('YES')

sol()