# 0x03강 - 배열
### 브론즈
- 10808 알파벳 개수
```python
name = list(input())
ls = [0]*26
al_ls = [chr(i) for i in range(ord('a'), ord('z')+1)]
for i in name:
  ls[al_ls.index(i)] += 1
for i in ls:
  print(i, end = ' ')
```
- 2577 숫자의 개수
```python
B = 1
for i in range(3):
  A = int(input())
  B *= A
num_list = list(str(B))
for i in range(0, 10):
  print(num_list.count(str(i)))
```
- 13300 방 배정
```python
from collections import Counter
N, K = map(int, input().split())
ls = []
for i in range(N):
    ls.append(tuple(input().split()))

cnt = Counter(ls)
room = 0

for key, value in cnt.items():
    if value <= K:
        room += 1
    elif value%K != 0 :
        room += value//K + 1
    else:
        room += value//K
print(room)
```
- 11328 Strfry
```python
T = int(input())
cnt = 0
for i in range(T):
    A, B = map(str, input().split())
    A = sorted(A)
    B = sorted(B)
    print('Possible' if A == B else 'Impossible') 
```
- 1919 애너그램 만들기
```python
A = list(input())
B = list(input())
al_ls = [chr(i) for i in range(ord('a'), ord('z')+1)]
cnt_A = [0]*26
cnt_B = [0]*26
cnt = 0
for i in range(len(A)):
    for j in range(len(al_ls)):
        if A[i] == al_ls[j]:
            cnt_A[j] += 1

for i in range(len(B)):
    for j in range(len(al_ls)):
        if B[i] == al_ls[j]:
            cnt_B[j] += 1

for i in range(26):
    if cnt_A[i] - cnt_B[i] != 0:
        cnt += abs(cnt_A[i] - cnt_B[i])
print(cnt)
```
### 실버
- 1475 방 번호
```python
import math
N = list(input())

num_ls = [0]*11

for i in N:
    num_ls[int(i)] += 1

num_ls[10] = int(math.ceil((num_ls[6] + num_ls[9])/2))
num_ls[6] = 0
num_ls[9] = 0

print(max(num_ls))
```
- 3273 두수의 합
```python
# 중첩 for 문을 통한 모든 경우의 수 탐색은 시간 초과가 되기 때문에 수들을 정렬 후, 가장 큰 값과 작은 값을 더하는 것 부터 시작해서, X보다 크면 큰수를 하나씩 줄이고 X보다 작으면 작은 수를 하나씩 늘려가는 방식으로 훨신 적은 경우의 수를 탐색하도록 하였다.
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
```