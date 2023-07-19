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
