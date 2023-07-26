N = int(input())
ls = list(map(int, input().split()))
ls_stack = []
rlt = []
cnt = 0

ls_stack.append([ls.pop(-1), -1])
rlt.append(ls_stack[0][1])


for i in range(N-1):
    temp_index = i

    temp_item = ls.pop(-1)

    while ls_stack[temp_index][0] <= temp_item:

        if ls_stack[temp_index][1] == -1:
            ls_stack.append([temp_item, -1])
            rlt.append(-1)
            break

        else:
            temp_index = ls_stack[temp_index][1]

    else:
        ls_stack.append([temp_item, temp_index])
        rlt.append(ls_stack[temp_index][0])

for i in rlt[::-1]:
    print(i, end = ' ') 