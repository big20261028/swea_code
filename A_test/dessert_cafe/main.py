import sys
sys.stdin = open('sample_input.txt','r')

def is_in_range(x,y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

# 현재 좌표 x,y / 시작 좌표 st_pos/ 여태 지나온 디저트들 temp / 방향 dr
def dfs(x,y,st_pos,temp,dr):
    global max_val

    # 다음 이동 좌표 확인
    nx = x + dxy[dr][0]
    ny = y + dxy[dr][1]

    # 시작 좌표와 현재 좌표가 같고, 한바퀴 돌고 왔으면
    if nx == st_pos[0] and ny == st_pos[1] and len(temp) >= 4:
        max_val = max(max_val,len(temp))
        return

    # 다음에 이동할 좌표가 matrix를 벗어 났는지, 이미 먹은 디저트인지 확인 후 리턴
    # 이미 방향을 정하고 들어왔음
    if not (is_in_range(nx,ny)) or matrix[nx][ny] in temp:
        return

    # 먹은 디저트 목록에 추가
    temp.append(matrix[nx][ny])
    
    # 다음 경로 탐색
    dfs(nx,ny,st_pos,temp,dr)

    # 방향 전환이 가능하면 1회 꺾은 경로로 탐색
    if dr < 3:
        dfs(nx,ny,st_pos,temp,dr+1)

    # 계산완료, 백트래킹 실행
    temp.pop()


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N)]

    # 순서 : 우하 -> 좌하 -> 좌상 -> 우상
    # 좌상단부터 우하단까지 이동하며 모든 경로를 탐색함
    # 고로 해당 좌표의 아래 대각선 위치를 시작 지점으로 하는 경로들만 탐색하면
    # 모든 경우의 수와 같다고 볼 수 있음
    dxy = [ (1, 1), (1, -1), (-1, -1), (-1, 1) ]
    max_val = -1


    for i in range(N):
        for j in range(N):
            st_pos = (i,j)
            dfs(i,j,st_pos,[matrix[i][j]],0)
    print(f'#{tc} {max_val}')