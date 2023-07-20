B = 1
for i in range(3):
  A = int(input())
  B *= A
num_list = list(str(B))
for i in range(0, 10):
  print(num_list.count(str(i)))
