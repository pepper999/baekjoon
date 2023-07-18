import sys
input = sys.stdin.readline
from collections import Counter
M = int(input())
ls_M = Counter(map(int, input().split()))
N = int(input())
for i in list(map(int, input().split())):
    print(ls_M[i], end = ' ')

