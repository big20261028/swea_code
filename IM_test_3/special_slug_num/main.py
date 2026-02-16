import sys
sys.stdin = open('sample_input.txt','r')

def make_slug(x,y,matrix):
    move_cnt = 0
    num = 2
    while True:
        dr = dxy[move_cnt % 4]
        m = move_cnt // 2 + 1
        for n in range(m):
            nx, ny = x + dr[0], y + dr[1]
            if not (0 <= nx < N and 0 <= ny < N):
                return
            x,y = nx,ny
            matrix[x][y] = num
            num += 1
        move_cnt += 1

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [ [0]*N for _ in range(N)]

    x,y = N//2,N//2
    matrix[x][y] = 1

    dxy = [ (0,-1),(1,0),(0,1),(-1,0) ]
    make_slug(x,y,matrix)

    print(f'#{tc}')
    for row in matrix:
        print(' '.join(map(str,row)))