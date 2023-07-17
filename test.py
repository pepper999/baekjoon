N = int(input())
mem = []
for i in range(N):
    mem.append(list(input().split()))
mem.sort(key = lambda a:int(a[0]))
for i in range(N):
    print(mem[i][0], mem[i][1])