import sys
sys.stdin = open('sample.txt','r')

T = int(input())
'''
가장 빠른 길을 찾아야하는 문제

heapq 사용법
heapq.heappush(넣을 리스트, 데이터)
heapq.heappop(뺄 리스트)

'''
import heapq

for test_case in range(1,T+1):
    n = int(input())
    # 0: 빈공간, 1:장애물, 2:소용돌이
    matrix = [ list(map(int,input().split())) for _ in range(n) ]

    hq = []

    start = tuple(map(int,input().split()))
    end = tuple(map(int,input().split()))

    dxy = [ (1,0),(-1,0),(0,1),(0,-1) ]

    #visited = [ list(0 for _ in range(n)) for _ in range(n) ]
    distance = [[float('inf')] * n for _ in range(n)]

    # 시간, x, y
    heapq.heappush(hq,[0,start[0],start[1]])
    distance[start[0]][start[1]] = 0

    result = -1
    while hq:
        t,x,y = heapq.heappop(hq)
        if end == (x,y):
            result = t
            break

        if distance[x][y] < t:
            continue

        for dx,dy in dxy:
            nx = x + dx
            ny = y + dy
            nt = t+1

            if 0 <= nx < n and 0 <= ny < n:

                if matrix[nx][ny] == 1: continue

                if matrix[nx][ny] == 2:
                    while (nt-1) % 3 != 2:
                        nt += 1
                    # if t % 3 == 0:
                    #     nt += 2
                    # elif t % 3 == 1:
                    #     nt += 1

                if nt < distance[nx][ny]:
                    distance[nx][ny] = nt
                    heapq.heappush(hq, (nt, nx, ny))

                # visited[nx][ny] = True
                # heapq.heappush(hq,[nt,nx,ny])

    print(f"#{test_case} {result}")


