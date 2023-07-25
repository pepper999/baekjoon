import sys
input = sys.stdin.readline

class stack:
    def __init__(self):
        self.top = []

    
    def push(self, item):
        self.top.append(item)
    
    def pop(self):
        self.top.pop(-1)
    
    def peek(self):
        if not self.empty():
            return self.top[-1]
        else:
            return 0
    
    def empty(self) -> bool:
        return len(self.top) == 0

skt = stack()

N = int(input())
ls = list(map(int, input().split()))
cnt = 0
j = 0
for i in ls:
    if skt.peek() < i:
        print(cnt)
        skt.push(i)
        j += 1
    elif skt.peek() > i:
        while skt.peek() <= i:
            skt.pop(i)
            cnt += 1