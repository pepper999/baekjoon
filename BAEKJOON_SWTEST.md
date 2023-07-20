# SW역량테스트 준비 기출문제
### 브론즈 단계
- 13458 시험 감독
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
- 2309 일곱 난쟁이
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
- 5566 주사위 게임
```python
ls_board = []
ls_dice = []
cnt = 0
N, M = map(int, input().split())
for i in range(N):
    ls_board.append(int(input()))
for i in range(M):
    ls_dice.append(int(input()))

for j in range(M):
    try:
        cnt += ls_dice[j]
        cnt += ls_board[cnt]
    except:
        print(j+1)
        break
    if cnt >= N-1:
        print(j+1)
        break
```
### 실버단계
- 1331 나이트투어
```python
from collections import Counter
import sys

ChessBoard = []
knight = []
for j in range(1,7):
    ChessBoard.append([f'{chr(i)}{j}' for i in range(ord('A'),ord('G'))])

for i in range(36):
    knight.append(input())

cnt = Counter(knight)

knight.append(knight[0])

for i in list(cnt.values()):
    if i > 1:
        print('Invalid')
        sys.exit()


for i in range(36):
    if abs(int(knight[i+1][1]) - int(knight[i][1])) == 2 and abs(int(ord(knight[i+1][0])) - int(ord(knight[i][0]))) == 1:
        pass
    elif abs(int(knight[i+1][1]) - int(knight[i][1])) == 1 and abs(int(ord(knight[i+1][0])) - int(ord(knight[i][0]))) == 2:
        pass
    else :
        print('Invalid')
        sys.exit()

print('Valid')
```
- 1026 보물
```python
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

gop = 0
A.sort()
B.sort()
B.reverse()
for i in range(N):
    gop += A[i] * B[i]
print(gop)
```
- 3048 개미
```python
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
ant1 = list(input().rstrip('\n'))
ant2 = list(input().rstrip('\n'))
T = int(input())

ant1.reverse()
ant_total = ant1 + ant2

for i in range(T):
    for i in range(len(ant_total) - 1):
        if ant_total[i] in ant1 and ant_total[i+1] in ant2: # 각 개미가 만나면
            ant_total[i], ant_total[i+1] = ant_total[i+1], ant_total[i] #각 개미의 자리를 변경
        
            if ant_total[i+1] == ant1[-1]:
                break

print(''.join(ant_total))
```
- 9372 상근이의 여행
```python

```
