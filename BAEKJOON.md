# 백준 문제풀이
### 기타
- 1076 저항
```python
ls1 = ['balck', 'brown','red','orange','yellow','green','blue','violet','grey','white']
ls2 = [10**i for i in range(len(ls1))]

A = str(input())
B = str(input())
C = str(input())

print(str(ls1.index(A)) + str(ls1.index(B)))
```
- 카운팅 정렬
```python
def counting(arr):
    m = max(arr)
    cnt = [0]*(m+1) # 최대수 + 1 크기의 count 리스트 형성
    for i in arr:
        cnt[i] += 1 # 각 수의 갯수를 count 리스트의 위치에 할당
    for i in range(1, len(cnt)):
        cnt[i] += cnt[i-1] # 누적 갯수 합계
    result = [0]*(len(arr)) # 결과 리스트 형성

    for num in arr:
        idx = cnt[num] # 각 수의 갯수의 위치 할당
        result[idx - 1] = num # 결과 리스트에 각 숫자를 배치
        cnt[num] -= 1 # count 리스트에 할당 된 숫자를 차감
    return result
```
- 13458 시험감독
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

