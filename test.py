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

