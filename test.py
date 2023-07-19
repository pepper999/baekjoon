
ls = []
for i in range(9):
    ls.append(int(input()))

for i in range(8):
    for j in range(i+1, 9):
        sum_ = sum(ls) - (ls[i] + ls[j])
        if sum_ == 100:
            pnt1, pnt2 = i, j
    
ls.pop(pnt1)
ls.pop(pnt2-1)
ls.sort()

for i in ls:
    print(i)

    