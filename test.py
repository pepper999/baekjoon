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

