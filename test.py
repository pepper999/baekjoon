chess_board = []

for j in range(1,9):
    chess_board.append([f'{chr(i)}{j}' for i in range(ord('A'), ord('H')+1)])

king, stone, N = input().split()
for i in range(8):
    if king in chess_board[i]: 
        king = [i, chess_board[i].index(king)]
    if stone in chess_board[i]:
        stone = [i, chess_board[i].index(stone)]


N = int(N)

for i in range(N):
    move = input()
    if move == 'T':
        if king[0] < 7:
            king[0] += 1
        if king == stone:
            if stone[0] < 7:
                stone[0] += 1
            else:
                king[0] -= 1
    elif move == 'B':
        if king[0] > 0:
            king[0] -= 1
        if king == stone:
            if stone[0] > 0:
                stone[0] -= 1
            else:
                king[0] += 1
    elif move == 'R':
        if king[1] < 7:
            king[1] += 1
        if king == stone:
            if stone[1] < 7:
                stone[1] += 1
            else:
                king[1] -= 1
    elif move == 'L':
        if king[1] > 0:
            king[1] -= 1
        if king == stone:
            if stone[1] > 0:
                stone[1] -= 1
            else:
                king[1] += 1    
    elif move == 'RT':
        if king[1] < 7 and king[0] < 7:
            king[1] += 1
            king[0] += 1
            if king == stone:
                if stone[1] < 7 and stone[0] <7:
                    stone[1] += 1
                    stone[0] += 1
                else:
                    king[1] -= 1
                    king[0] -= 1
    elif move == 'LT':
        if king[1] > 0 and king[0] < 7:
            king[1] -= 1
            king[0] += 1
            if king == stone:
                if stone[1] > 0 and stone[0] <7:
                    stone[1] -= 1
                    stone[0] += 1
                else:
                    king[1] += 1
                    king[0] -= 1
    elif move == 'RB':
        if king[1] < 7 and king[0] > 0:
            king[1] += 1
            king[0] -= 1
            if king == stone:
                if stone[1] < 7 and stone[0] > 0:
                    stone[1] += 1
                    stone[0] -= 1
                else:
                    king[1] -= 1
                    king[0] += 1
    elif move == 'LB':
        if king[1] > 0 and king[0] > 0:
            king[1] -= 1
            king[0] -= 1
            if king == stone:
                if stone[1] > 0 and stone[0] > 0:
                    stone[1] -= 1
                    stone[0] -= 1
                else:
                    king[1] += 1
                    king[0] += 1

print(chess_board[king[0]][king[1]])
print(chess_board[stone[0]][stone[1]])