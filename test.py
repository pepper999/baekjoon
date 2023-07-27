N = int(input())
ls = []
ls_stack = []
for i in range(N):
    ls.append(int(input()))

cnt = 0
ls_stack.append([ls.pop(-1), -1, 0, 0])
rlt = 0
j = 1
for i in range(N-1):
    local_cnt = 0
    temp_index = i
    temp_item = ls.pop(-1)

    while ls_stack[temp_index][0] <= temp_item:
        if ls_stack[temp_index][0] == temp_item:
            local_cnt += 1
            temp_index = ls_stack[temp_index][1]
        elif ls_stack[temp_index][1] == -1:
            ls_stack.append([temp_item, -1, local_cnt, j])
            j += 1
            break
        else:
            temp_index = ls_stack[temp_index][1]
    else:
        ls_stack.append([temp_item, temp_index, local_cnt, j])
        j += 1
    

print(ls_stack)