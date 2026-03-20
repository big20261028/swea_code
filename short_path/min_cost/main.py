import sys

sys.stdin = open('sample_input.txt', 'r')

from heapq import heappush, heappop

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]


def bfs(st_x, st_y, end_x, end_y):
    min_fuel = [[float('inf')] * N for _ in range(N)]
    min_fuel[st_x][st_y] = 0

    hq = [(0, (st_x, st_y))]

    while hq:
        cost, (x, y) = heappop(hq)

        if (x, y) == (end_x, end_y):
            return cost

        if min_fuel[x][y] < cost:
            continue

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue

            need_cost = 1
            if matrix[x][y] < matrix[nx][ny]:
                need_cost += matrix[nx][ny] - matrix[x][y]
            next_cost = cost + need_cost

            if next_cost < min_fuel[nx][ny]:
                min_fuel[nx][ny] = next_cost
                heappush(hq, (next_cost, (nx, ny)))


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]

    result = bfs(0, 0, N - 1, N - 1)

    print(f'#{tc} {result}')