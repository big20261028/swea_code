import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dxy = [(1,0),(-1,0),(0,1),(0,-1)]

def find_start(matrix):
    for i in range(16):
        for j in range(16):
            if matrix[i][j] == 2:
                return i, j

def bfs(st_x,st_y):
    queue = deque()
    queue.append((st_x, st_y))
    matrix[st_x][st_y] = 1

    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if not (0 <= nx < 16 and 0 <= ny < 16):
                continue
            if matrix[nx][ny] == 1:
                continue
            if matrix[nx][ny] == 3:
                return 1
            matrix[nx][ny] = 1
            queue.append((nx, ny))
    return 0


for tc in range(1,11):
    N = int(input())
    matrix = [ list(map(int, input())) for _ in range(16)]

    st_x, st_y = find_start(matrix)
    result = bfs(st_x, st_y)
    print(f'#{tc} {result}')
