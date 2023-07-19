def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

def gcdarr(list):
    gcdarr = ls_p[0]
    for i in range(len(ls_p)):
        gcdarr = gcd(gcdarr, ls_p[i])
    return gcdarr

N = int(input())
ls = []
ls_p = []
for i in range(N):
    ls.append(int(input()))
for i in range(N-1):
    ls_p.append(ls[i+1] - ls[i])

print(gcdarr(ls_p))



    