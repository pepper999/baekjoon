# 백준 단계별로 풀어보기(1~3)
### 백준 2단계
- 2884 알람시계
```python
H, M = map(int, input().split())
min = H*60 + M
min -= 45
H = min//60
M = min%60
if H < 0:
    H += 24

print(H, M)
```
- 2525 오븐 시계
```python
H, M = map(int, input().split())
min = H*60 + M
min += int(input())
H = min//60
M = min%60
if H > 23:
    H -= 24
print(H, M)
```
- 10818 최소, 최대
```python
N = int(input())
num = list(map(int, input().split()))
print(min(num), max(num))
```
- 10812 공 바꾸기
```python
N, M = map(int, input().split())
ls = [i for i in range(N)]
for i in range(M):
    i, j = map(int, input().split())
    temp = ls[i]
    ls[i] = ls[j]
    ls[i] = temp
for i in range(len(ls)):
    print(ls[i])
```