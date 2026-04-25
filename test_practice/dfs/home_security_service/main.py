import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import deque

T = int(input())

dxy = [ (1,0), (-1,0), (0,1), (0,-1), ]

def bfs(c_x, c_y):
    global max_house_cnt

    queue = deque()
    queue.append((c_x, c_y, 0))
    visited = set()
    visited.add((c_x, c_y))

    home_cnt = 0
    if matrix[c_x][c_y] == 1:
        home_cnt += 1
    max_house_cnt = max(max_house_cnt, home_cnt)

    while queue:
        x, y, dist = queue.popleft()
        K = dist + 2
        cost = K ** 2 + (K - 1) ** 2

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if (nx,ny) in visited:
                continue

            visited.add((nx,ny))

            if matrix[nx][ny] == 1:
                home_cnt += 1
                if cost <= home_cnt * M:
                    max_house_cnt = max(max_house_cnt, home_cnt)

            queue.append((nx, ny, dist + 1))


for tc in range(1,T+1):
    N, M = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N)]

    max_house_cnt = float('-inf')

    for i in range(N):
        for j in range(N):
            bfs(i,j)

    print(f'#{tc} {max_house_cnt}')