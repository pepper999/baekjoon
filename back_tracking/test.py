N = int(input())
visited = [0] * (N+1)
rlt = 10 ** 5
matrix = []
for i in range(N):
    matrix.append(list(map(int, input().split())))

def back(L, num):
    global rlt
    if L == N // 2:
        start = 0
        link = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j] and i != j:
                    start += matrix[i][j]
                    start += matrix[j][i]
                elif not visited[i] and not visited[j] and i != j:
                    link += matrix[i][j]
                    link += matrix[j][i]
                if abs(start - link) < rlt:
                    rlt = abs(start - link)
        return rlt
    for i in range(num, N+1):
        if not visited[i]:
            visited[i] = 1
            back(L+1, num+1)
            visited[i] = 0

print(rlt)