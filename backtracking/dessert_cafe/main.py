import sys
sys.stdin = open('sample_input.txt', 'r')

# 좌하, 우하, 우상, 좌상
dxy = [(1, -1), (1, 1), (-1, 1), (-1, -1)]

def dfs(st_pos, x, y, dr, eaten):
    global max_val

    if st_pos == (x, y) and len(eaten) >= 4:
        max_val = max(max_val, len(eaten))
        return

    dx, dy = dxy[dr]
    nx, ny = x + dx, y + dy
    if 0 <= nx < N and 0 <= ny < N:
        if matrix[nx][ny] not in eaten:
            dfs(st_pos, nx, ny, dr, eaten + [matrix[nx][ny]])

    if dr < 3:
        dr += 1
        dx, dy = dxy[dr]
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < N:
            if matrix[nx][ny] not in eaten:
                dfs(st_pos, nx, ny, dr, eaten + [matrix[nx][ny]])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    max_val = -1
    for i in range(N-2):
        for j in range(1,N-1):
            dfs((i,j),i,j, 0, [])

    print(f'#{tc} {max_val}')
