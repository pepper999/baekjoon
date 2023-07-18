N, M = map(int, input().split())
N_ls = []
M_ls = []
cnt = 0

for i in range(N):
  N_ls.append(input())
for i in range(M):
  M_ls.append(input())

for i in M_ls:
  if i in N_ls:
    cnt += 1
print(cnt)