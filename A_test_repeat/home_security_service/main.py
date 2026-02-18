import sys
sys.stdin = open('sample_input.txt','r')
'''
손해 보지 않으면서 서비스를 가장 많은 집들에 제공하는 서비스 영역 찾기, 
서비스를 제공받는 집들의 수 출력

'''

from collections import deque
# 시작지점으로부터 떨어진 맨해튼 거리 계산
# 그 거리로 탐색 비용 계산, 여태 탐색한 데이터로 이익 계산

dxy = [ (1,0),(-1,0),(0,1),(0,-1) ]

def find_max_service(i,j):
    global max_val

    queue = deque()

    visited = [ [True] * N for _ in range(N) ]
    visited[i][j] = False
    queue.append((i,j))

    cnt = 0
    if matrix[i][j] == 1 : cnt += 1

    if cnt * M >= 1:
        max_val = max(max_val, cnt)

    while queue:
        x,y = queue.popleft()

        for dx,dy in dxy:
            nx,ny = x+dx,y+dy
            if not (0 <= nx < N and 0 <= ny < N and visited[nx][ny]):
                continue

            k = abs(i - nx) + abs(j - ny) + 1
            cost = k**2 + (k-1)**2

            if matrix[nx][ny] == 1: cnt += 1
            visited[nx][ny] = False

            profit = cnt * M

            if cost <= profit:
                max_val = max(max_val,cnt)

            queue.append((nx,ny))

T = int(input())
for tc in range(1,T+1):
    # 도시의 크기, 집 하나 당 이익
    N,M = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N)]

    max_val = 0
    for i in range(N):
        for j in range(N):
            find_max_service(i,j)

    print(f'#{tc} {max_val}')
