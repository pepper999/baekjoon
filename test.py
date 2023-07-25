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

for i in range(len(ls)):
        while skt.peek() < i and skt.peek() != 0:
            skt.pop()
        print(skt.peek())
        skt.push({i:ls[i]})
            
        
    else:
        skt.push(i)
        cnt = i
        print(cnt)