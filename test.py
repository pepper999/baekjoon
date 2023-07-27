N = int(input())
ls = []
stack_ls = []
for i in range(N):
    ls.append(int(input()))
ls.append(-1)
cnt = 0

for i in range(N):
    temp_long = -1
    temp_val = ls.pop(0)
    j = 0
    while temp_val >= ls[j]:
        if ls[j] == -1:
            break
        if temp_val >= temp_long and ls[j] >= temp_long:
            temp_long = ls[j]
            j += 1
            cnt += 1
        elif ls[j] < temp_long:
            break
    else:
        cnt += 1

print(cnt)