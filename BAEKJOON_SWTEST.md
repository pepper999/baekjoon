# SW역량테스트 준비 기출문제
### 브론즈 단계
- 시험 감독
```python
N = int(input())
A = list(map(int,input().split()))
B, C = map(int, input().split())
cnt = int(N)
for i in range(N):
    if A[i] - B > 0 and (A[i]-B)%C != 0:
        cnt += (A[i]-B)//C + 1
    if A[i] - B > 0 and (A[i]-B)%C == 0:
        cnt += (A[i]-B)//C
print(cnt)
```
- 일곱난쟁이
```python
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
```