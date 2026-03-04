import sys

sys.stdin = open('input.txt', 'r')

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def find_start_pos(matrix):
    for i in range(16):
        for j in range(16):
            if matrix[i][j] == 2:
                return i, j


def dfs(st_pos):
    stack = [st_pos]
    visited = [[False] * 16 for _ in range(16)]
    visited[st_pos[0]][st_pos[1]] = True
    flag = 0
    while not flag and stack:
        x, y = stack.pop()
        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < 16 and 0 <= ny < 16):
                continue
            if visited[nx][ny]:
                continue
            if matrix[nx][ny] == 1:
                continue

            if matrix[nx][ny] == 3:
                flag = 1
                break

            visited[nx][ny] = True
            stack.append((nx, ny))

    return flag


for tc in range(1, 11):
    n = int(input())
    matrix = [list(map(int, input())) for _ in range(16)]
    st_pos = find_start_pos(matrix)

    result = dfs(st_pos)
    print(f'#{tc} {result}')