N = int(input())
ls = []
ls_stack = []
cnt = 0
for i in range(N):
    ls.append(int(input()))
ls_stack.append([ls.pop(-1), -1])
for i in range(N-1):
    temp_index = i
    temp_item = ls.pop(-1)
    while ls_stack[temp_index][0] < temp_item:
        if ls_stack[temp_index][1] == -1:
            ls_stack.append([temp_item, -1])
            cnt += i +1
            break
        else:
            temp_index = ls_stack[temp_index][1]
    else:
        ls_stack.append([temp_item, temp_index])
        cnt += i - temp_index
print(cnt)

    