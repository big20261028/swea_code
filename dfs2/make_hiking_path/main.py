import sys
sys.stdin = open('sample_input.txt', 'r')

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def dfs(deps, pos, ability):
    global max_len
    max_len = max(max_len,deps)

    x,y = pos
    visited[x][y] = True
    h = 0
    if ability:
        h = K

    for dx, dy in dxy:
        nx, ny = x + dx, y + dy
        if not (0 <= nx < N and 0 <= ny < N):
            continue
        if visited[nx][ny]:
            continue
        for h_2 in range(h+1):
            if (matrix[nx][ny] - h_2) < matrix[x][y]:
                visited[nx][ny] = True
                if h_2:
                    matrix[nx][ny] -= h_2
                    dfs(deps+1, (nx, ny), False)
                    matrix[nx][ny] += h_2
                else:
                    dfs(deps + 1, (nx, ny), ability)
                visited[nx][ny] = False


T = int(input())
for tc in range(1, T+1):
    N, K = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]

    st_pos = []
    max_h = 0
    for i in range(N):
        for j in range(N):
            if matrix[i][j] > max_h:
                max_h = matrix[i][j]
                st_pos.clear()
                st_pos.append( (i,j) )
            elif matrix[i][j] == max_h:
                st_pos.append((i, j))

    max_len = 0
    for x,y in st_pos:
        visited = [[False]*N for _ in range(N)]
        dfs(1,(x,y),True)
    print(f'#{tc} {max_len}')

