import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

dxy = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]

def bfs(st_x, st_y):
    global click_cnt

    queue = deque()
    queue.append((st_x, st_y))

    while queue:
        x, y = queue.popleft()
        for dx,dy in dxy:
            nx,ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if visited[nx][ny]:
                continue
            if isinstance(matrix[nx][ny], int):
                visited[nx][ny] = True
                if matrix[nx][ny] == 0:
                    queue.append((nx,ny))
                    zero_pos_list.remove((nx,ny))

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 지뢰 *  지뢰없음 .
    matrix = [list(input()) for _ in range(N)]
    click_cnt = 0
    zero_pos_list = set()

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == '*': continue
            cnt = 0
            for dx,dy in dxy:
                nx,ny = i + dx, j + dy
                if not (0 <= nx < N and 0 <= ny < N):
                    continue
                if matrix[nx][ny] == '*':
                    cnt += 1
            matrix[i][j] = cnt
            if cnt == 0:
                zero_pos_list.add((i,j))

    visited = [ [False] * N for _ in range(N)]

    #print(len(zero_pos_list))

    while zero_pos_list:
        x,y = zero_pos_list.pop()
        visited[x][y] = True
        bfs(x,y)
        click_cnt += 1

    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                continue
            if matrix[i][j] == '*':
                continue
            click_cnt += 1


    print(f'#{tc} {click_cnt}')









