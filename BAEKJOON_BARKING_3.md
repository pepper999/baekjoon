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
from collections import Counter
T = int(input())
for i in range(T):
  A, B = list(map(str, input().split()))
  cnt_A = Counter(A)
  cnt_B = Counter(B)
  cnt = 0
  for key, value in cnt_A.items():
    if value != cnt_B[key]:
      print('Impossible')
      break
    cnt += 1
  if cnt == len(A):
    print('Possible')  
???
```