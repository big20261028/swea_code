import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import deque
from heapq import heappush, heappop

dxy = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def bfs(st_x, st_y, end_x, end_y):
    min_fuel = [ [False] * N for _ in range(N) ]
    min_fuel[0][0] = 0

    # queue = deque()
    # queue.append(( (st_x, st_y), 0 ))
    hq = [(0, (st_x, st_y))]
    while hq:
        cost, (x, y) = heappop(hq)

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue

            need_cost = 1
            if matrix[x][y] < matrix[nx][ny]:
                need_cost += matrix[nx][ny] - matrix[x][y]
            next_cost = cost + need_cost

            if (nx, ny) == (end_x, end_y):
                return next_cost

            if min_fuel[nx][ny] < need_cost:
                continue




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [ list(map(int, input().split())) for _ in range(N) ]