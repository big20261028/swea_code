import sys
sys.stdin = open('input.txt','r')

from heapq import heappop,heappush

dxy = [ (1,0),(-1,0),(0,1),(0,-1)]

def bfs():
    # 큐 , (소요시간, x, y)
    hq = []
    heappush(hq, (0,(0,0)))
    visited = [ [False] * N for _ in range(N) ]
    visited[0][0] = True

    while hq:
        # 가장 소요시간이 짧은 곳부터 탐색
        time, (x, y) = heappop(hq)
        for dx,dy in dxy:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < N):
                continue
            if visited[nx][ny]:
                continue
            if nx == N-1 and ny == N-1:
                return time
            visited[nx][ny] = True
            heappush(hq, (time + matrix[nx][ny], (nx, ny)))


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [ list(map(int,input())) for _ in range(N)]
    min_path = bfs()

    print(f'#{tc} {min_path}')