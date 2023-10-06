def find(a):
    if parents[a] != a:
        parents[a] = find(parents[a])
    return parents[a]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parents[b] = a
        size[a] += size[b]
    print(size[a])

T = int(input())
for t in range(T):
    F = int(input())
    parents = {}
    size = {}
    for f in range(F):
        friend1, friend2 = input().split()
        if friend1 not in parents:
            parents[friend1] = friend1
            size[friend1] = 1
        if friend2 not in parents:
            parents[friend2] = friend2
            size[friend2] = 1
        union(friend1, friend2)