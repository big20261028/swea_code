import sys
sys.stdin = open('sample_input.txt','r')

from collections import deque

def find_max_pos(i,j):
    time = 1

    visited = [ [True] * M for _ in range(N) ]

    queue = deque([[(i,j),time]])
    visited[i][j] = False

    pos_list = set()
    pos_list.add((i,j))

    while queue:
        (x,y),t = queue.popleft()
        #a = queue.popleft()
        #print(a)
        if t >= L : continue
        dr_list = pipe_dict[matrix[x][y]]
        for i in dr_list:
            dx,dy = dxy[i]
            nx,ny = x + dx, y + dy
            if not (0 <= nx < N and 0 <= ny < M and visited[nx][ny]):
                continue
            if matrix[nx][ny] == 0:
                continue
            require_path = filter_dict[i]

            dr_list_n = pipe_dict[matrix[nx][ny]]
            if require_path not in dr_list_n:
                continue

            queue.append([(nx,ny),t+1])
            visited[nx][ny] = False
            pos_list.add((nx,ny))

    return len(pos_list)

T = int(input())
for tc in range(1,T+1):
    # 터널 세로, 가로, 맨홀 위치 세로, 가로, 탈출 후 소요시간
    N,M,R,C,L = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]

    # 상 하 좌 우
    dxy = [ (-1,0),(1,0),(0,-1),(0,1)]

    # 구조물 데이터 dict
    pipe_dict = {
        # 상 하 좌 우
        1 : [0,1,2,3],
        2 : [0,1],
        3 : [2,3],
        4 : [0,3],
        5 : [1,3],
        6 : [1,2],
        7 : [0,2],
    }
    # 도착지 기준 뚫려있어야 할 위치
    filter_dict = {
        0 : 1, 1 : 0, 2 : 3, 3 : 2
    }

    max_pos = find_max_pos(R,C)

    print(f'#{tc} {max_pos}')
