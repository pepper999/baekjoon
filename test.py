N, M = map(int, input().split())
ls = [i+1 for i in range(N)]


for k in range(M):
    i, j = map(int, input().split())
    temp = ls[i-1]
    ls[i-1] = ls[j-1]
    ls[j-1] = temp
for i in range(len(ls)):
    print(ls[i], end = ' ')

