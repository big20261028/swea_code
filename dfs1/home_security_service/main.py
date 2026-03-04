import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import deque

dxy = [ (1, 0), (-1, 0), (0, 1), (0, -1) ]

def bfs(i, j):
    global max_val
    # x,y,거리
    queue = deque([[(i, j), 0]])
    visited = [[False] * N for _ in range(N)]
    visited[i][j] = True
    home_cnt = 0
    if matrix[i][j] == 1:
        home_cnt += 1
    max_val = max(max_val, home_cnt)

    while queue:
        (x, y), dist = queue.popleft()
        k = dist + 2
        cost = k**2 + (k-1)**2
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if visited[nx][ny]:
                continue
            if matrix[nx][ny] == 1:
                home_cnt += 1
                if cost <= home_cnt * M:
                    max_val = max(max_val, home_cnt)
            visited[nx][ny] = True
            queue.append([(nx, ny), (dist + 1)])


T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]
    # 모든 좌표를 기준으로 bfs 탐색, 최대 집의 수 구하기
    max_val = 0
    for i in range(N):
        for j in range(N):
            bfs(i, j)

    print(f'#{tc} {max_val}')