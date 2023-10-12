from collections import deque

def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 'R':
                rx, ry = i, j
            elif graph[i][j] == 'B':
                bx, by = i, j
    q.append((rx, ry, bx, by, 1))
    visited[rx][ry][bx][by] = True


def move(x, y, dx, dy):
    c = 0
    while graph[x + dx][y + dy] != '#' and graph[x][y] != 'O':
        x += dx
        y += dy
        c += 1
    return x, y, c


def bfs():
    while q:
        crx, cry, cbx, cby, cnt = q.popleft()
        if cnt > 10: break
        for i in range(4):
            nrx, nry, rc = move(crx, cry, *d[i])  
            nbx, nby, bc = move(cbx, cby, *d[i])  
            if graph[nbx][nby] != 'O':  
                if graph[nrx][nry] == 'O':  
                    print(cnt)
                    return
                if nrx == nbx and nry == nby:  
                    if rc > bc:  
                        nrx -= d[i][0]
                        nry -= d[i][1]
                    else:
                        nbx -= d[i][0]
                        nby -= d[i][1]
                if not visited[nrx][nry][nbx][nby]:
                    visited[nrx][nry][nbx][nby] = True
                    q.append((nrx, nry, nbx, nby, cnt + 1))
    print(-1)  # 결국 빨간 구슬 구멍에 못 넣었으면 실패


d = [(-1, 0), (1, 0), (0, 1), (0, -1)]
q = deque()
n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]

init()
bfs()