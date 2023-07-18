# 백준 단계별로 풀어보기(13-15)
### 백준 13단계
- 2750 수 정렬하기
```python
N = int(input())
ls = []
for i in range(N):
    ls.append(int(input()))

ls.sort()
for i in range(N):
    print(ls[i])
```
- 2587 대푯값2
```python
ls = []
for i in range(5):
    ls.append(int(input()))
ls.sort()
print(sum(ls)/5)
print(ls[2])
```
- 25305 커트라인
```python
N, K = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort(reverse=True)
print(ls[K-1])
```
- 2751 수 정렬하기 2
```python
import sys
input = sys.stdin.readline

N = int(input())
ls = []
for i in range(N):
    ls.append(int(input()))
ls.sort()
for i in range(N):
    print(ls[i])   
```
- 10989 수 정렬하기 3
```python
import sys
input = sys.stdin.readline

N  = int(input())
num = [0] * 10001

for i in range(N):
    temp = int(input())
    num[temp] += 1

for i in range(10001):
    if num[i] != 0:
        for j in range(num[i]):
            print(i)
```
- 1427 소트인사이드
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

num = list(map(int, str(input())))
rlt = counting(num)
for i in range(len(rlt)):
    print(rlt[-i-1], end = '')
```
- 11650 좌표 정렬하기
```python
N = int(input())
ls = []
for i in range(N):
    ls.append(list(map(int, input().split())))

ls.sort()
for i in range(N):
    print(ls[i][0], end = ' ')
    print(ls[i][1])
```
- 11651 좌표 정렬하기2
```python
import sys
input = sys.stdin.readline

N = int(input())
ls = []
for i in range(N):
    a, b = map(int, input().split())
    ls.append([b, a])
ls.sort()
for i in range(N):
    print(ls[i][1], end = ' ')
    print(ls[i][0])   
```
- 1181 단어 정렬
```python
import sys
input = sys.stdin.readline

N = int(input())
ls = []

for i in range(N):
    ls.append(input().strip())
ls = list(set(ls))
ls.sort()
ls.sort(key = len)

for i in ls:
    print(i)
```
- 10814 나이순 정렬
```python
N = int(input())
mem = []
for i in range(N):
    mem.append(list(input().split()))
mem.sort(key = lambda a:int(a[0])) # lambda 값으로 특정 기준을 할당!
for i in range(N):
    print(mem[i][0], mem[i][1])

```
- 18870 좌표압축
```python

N = int(input())
spt = list(map(int, input().split()))
spt2 = list(set(spt))
spt2.sort()

spt_dict = {}
for i in range(len(spt2)):
    spt_dict[spt2[i]] = i

for i in spt:
    print(spt_dict[i], end = ' ')
# list 의 인덱스에 의존한 인덱싱은 시간복잡도가 높아 시간이 오래걸리기 때문에 dict 으로 처리하는 것이 유리
```
### 백준 14단계
- 10815 숫자 카드
```python
import sys
input = sys.stdin.readline

N = int(input())
N_ls = list(map(int, input().split()))
N_ls.sort()
M = int(input())
M_ls = list(map(int, input().split()))

def check_mid(list1, num, start, end): # 데이터를 크기 순서대로 정렬 후, 반으로 나누어 검정하므로 시간 감소!
    while(end >= start):
        mid = (start+end)//2
        if num == list1[mid]:
            return True
        elif num > list1[mid]:
            start = mid+1
        else: end = mid-1
    return False

for i in range(M):
    if check_mid(N_ls, M_ls[i], 0, N-1) is not False:
        print(1, end = ' ')
    else:
        print(0, end = ' ')
```
- 14425 문자열 집합
```python
N, M = map(int, input().split())
N_ls = []
M_ls = []
cnt = 0

for i in range(N):
    N_ls.append(input())
for i in range(M):
    M_ls.append(input())

for i in M_ls:
    if i in N_ls:
        cnt += 1
print(cnt)
```
- 7785 회사에 있는 사람
```python
import sys
input = sys.stdin.readline
N = int(input())
log = dict()
for i in range(N):
  a, b = input().split()
  log[a] = b

log = dict(sorted(log.items(), key = lambda item: item[0], reverse = True)) # item[0] => 딕셔너리의 key

for key, val in log.items():
  if val == 'enter':
    print(key)
```
- 1620 포켓몬 마스터
```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
po_dict = dict()
for i in range(N):
    K = input()
    po_dict[i+1] = K

po_dict2 = {v:k for k,v in po_dict.items()}

for i in range(M):
    name = input()
    try:
        print(po_dict2[name])
    except:
        print(po_dict[int(name)].strip('\n'))
```
- 10816 숫자 카드 2
```python
import sys
input = sys.stdin.readline
from collections import Counter
M = int(input())
ls_M = Counter(map(int, input().split()))
N = int(input())
for i in list(map(int, input().split())):
    print(ls_M[i], end = ' ')
```