N = int(input())
spt = list(map(int, input().split()))
spt2 = list(set(spt))
spt2.sort()

spt_dict = {}
for i in range(len(spt2)):
    spt_dict[spt2[i]] = i

for i in spt:
    print(spt_dict[i], end = ' ')