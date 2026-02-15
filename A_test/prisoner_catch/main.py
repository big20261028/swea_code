import sys
sys.stdin = open('sample_input.txt','r')

from collections import deque

def find_place(R,C,L):

    # 큐를 이용한 BFS 탐색 실시
    queue = deque()

    # 현재 데이터를 queue에 등록
    st_data = {
        'pos' : (R,C),
        'time' : 1,
    }
    queue.append(st_data)
    visited = [[True] * M for _ in range(N)]
    place = set()

    # 현재 위치를 visited, place에 등록
    visited[R][C] = False
    place.add((R,C))

    # queue가 텅 빌때까지 반복

    while queue:
        # 큐의 맨 앞에서 위치/시간 데이터 하나 빼오기
        target = queue.popleft()
        x,y = target['pos']
        t = target['time']
        # 만약 시간 데이터가 L과 같으면 continue
        # 데이터만 pop 했기 때문에 사라짐
        if t == L: continue

        # 현재 좌표 x,y에서 갈 수 있는 위치 파악
        directions = tunnel_fabrics[matrix[x][y]]

        # 갈 수 있는 위치 좌표들을 조사, 통로가 이어져 있으면 추가
        for direction in directions:
            # 이동할 좌표 값
            nx = x + dxy[direction][0]
            ny = y + dxy[direction][1]
            # 좌표값이 범위 안에 있는지 검사
            if not (0 <= nx < N and 0 <= ny < M):
                continue
            # 이미 방문한 곳이라면 방문하지 않음
            if not visited[nx][ny]:
                continue
            # 이동할 좌표값이 0이면 갈 수 없음, 컨티뉴
            if matrix[nx][ny] == 0:
                continue

            # 이어져 있어야 할 좌표값 W E S N
            necessary_connect = arrive_direction[direction]
            # 이동할 좌표값의 구조물 타입
            tunnel_type = tunnel_fabrics[matrix[nx][ny]]
            # 구조물 타입에 이어져 있어야 할 좌표값이 없으면 continue
            if necessary_connect not in tunnel_type:
                continue

            # 이어져 있다면 해당 좌표값과 시간 정보를 queue에 append
            data = {
                'pos' : (nx, ny),
                'time' : t+1,
            }
            visited[nx][ny] = False
            place.add((nx, ny))
            queue.append(data)

    # 모든 경로 탐색 완료
    # place의 길이를 return
    return len(place)

T = int(input())
for tc in range(1,T+1):
    # 세로크기, 가로크기, 맨홀 세로위치, 맨홀 가로위치, 탈출 소요시간
    N,M,R,C,L = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    # 터널 구조물 타입 정리
    tunnel_fabrics = {
        1 : ['W','E','S','N'], # 상하좌우
        2 : ['S','N'],         # 상하
        3 : ['W','E'],         # 좌우
        4 : ['E','N'],         # 상우
        5 : ['E','S'],         # 하우
        6 : ['W','S'],         # 하좌
        7 : ['W','N'],         # 상좌
    }
    # 출발좌표 : 도착좌표
    arrive_direction = {
        'W' : 'E',
        'E' : 'W',
        'S' : 'N',
        'N' : 'S',
    }
    # 방향 별 dxy값
    dxy = {
        'W' : (0,-1),
        'E' : (0,1),
        'S' : (1,0),
        'N' : (-1,0),
    }



    # 1시간일때 맨홀로 지하로 내려감
    # 고로, 2시간일때부터 탈주범의 이동범위가 늘어남
    result = find_place(R,C,L)

    print(f'#{tc} {result}')