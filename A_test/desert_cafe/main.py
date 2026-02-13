import sys
sys.stdin = open('sample_input.txt','r')

def is_in_range(x,y):
    if 0 <= x < N and 0 <= y < N:
        return True
    return False

def find_max_dessert(deps,pos,total,move_cnt):
    global max_val
    if deps != 0 and start_pos == pos:
        if move_cnt[0] == move_cnt[2] and move_cnt[1] == move_cnt[3]:
            max_val  = max(max_val,sum(total))
        return

    for i in range(4):
        nx = pos[0] + dxy[i][0]
        ny = pos[1] + dxy[i][1]
        if is_in_range(nx,ny) and visited[nx][ny] and matrix[nx][ny] not in total:
            visited[nx][ny] = False
            total.append(matrix[nx][ny])
            move_cnt[i] += 1
            find_max_dessert(deps+1,(nx,ny),total,move_cnt)
            visited[nx][ny] = True
            total.pop()
            move_cnt[i] -= 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]

    # 순서 : 좌상, 우상, 우하, 좌하
    dxy = [ (-1,-1),(-1,1),(1,1),(1,-1) ]

    max_val=0
    move_cnt = [0, 0, 0, 0]
    total = []
    visited = [[True] * N for _ in range(N)]

    for x in range(N):
        for y in range(N):
            start_pos = (x,y)
            find_max_dessert(0,(x,y),total,move_cnt)

    if max_val == 0:
        max_val = -1

    print(f'#{tc} {max_val}')
    