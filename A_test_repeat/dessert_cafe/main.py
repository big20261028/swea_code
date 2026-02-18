import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
# 서남, 동남, 동북, 서북
dxy = [ (1,-1),(1,1),(-1,1),(-1,-1) ]

def find_max_dessert(x,y,st_pos,ate_list,dr):
    global max_val

    if dr == 3 and st_pos == (x,y):
        max_val = max(max_val,len(ate_list))
        return

    dx,dy = dxy[dr]

    nx,ny = x + dx, y + dy

    if not (0<=nx<N and 0<=ny<N):
        return

    if matrix[nx][ny] in ate_list:
        return

    find_max_dessert(nx,ny,st_pos,ate_list + [matrix[nx][ny]], dr)

    if dr < 3:
        find_max_dessert(nx, ny, st_pos, ate_list + [matrix[nx][ny]], dr+1)

for tc in range(1,T+1):
    # 지역 한변의 길이
    N = int(input())
    # 디저트 카페 정보
    matrix = [ list(map(int,input().split())) for _ in range(N) ]

    max_val = -1

    for i in range(N):
        for j in range(N):
            find_max_dessert(i, j, (i,j) ,[], 0)

    print(f'#{tc} {max_val}')
