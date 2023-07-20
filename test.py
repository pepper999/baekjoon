
air_ls = []
N, M = map(int, input().split())
pnt = 0
ls = [0]*N
for i in range(N):
    A, B = map(str, input().split())
    air_ls.append([A, B])
    air_ls.append([B, A])

print(air_ls)
