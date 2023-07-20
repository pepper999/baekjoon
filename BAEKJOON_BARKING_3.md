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
N, M = map(int, input().split())
```