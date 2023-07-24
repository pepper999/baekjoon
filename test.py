N = int(input())
num = list(map(int, input().split()))
X = int(input())
cnt = 0
num.sort()
A = 0
B = N-1
while B > A:
    if num[A] + num[B] > X:
        B -= 1
    elif num[A] + num[B] < X:
        A += 1
    elif num[A] + num[B] == X:
        cnt += 1
        B -= 1
        A += 1

print(cnt)