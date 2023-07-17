N = int(input())

n_5, n_3 = 0, 0
num_ls = []

for i in range(N):
    for j in range(N):
        num = 5*i + 3*j
        if num == N:
            num_ls.append(i + j)

if len(num_ls) == 0:
    print(-1)
else:
    print(min(num_ls))