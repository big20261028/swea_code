import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix =[ [0]*N for _ in range(N) ]

    # 동, 남, 서, 북
    dxy = [(0,1),(1,0),(0,-1),(-1,0)]
    dr = 0
    x,y = 0,0

    matrix[0][0] = 1

    cnt = 1
    while cnt < N**2:
        cnt += 1
        dx,dy = dxy[dr]
        nx,ny = x+dx,y+dy
        if not (0 <= nx < N and 0 <= ny < N and matrix[nx][ny] == 0):
            dr = (dr + 1) % 4
            dx, dy = dxy[dr]
            nx, ny = x + dx, y + dy

        matrix[nx][ny] = cnt
        x,y = nx,ny
    print(f'#{tc}')
    for row in matrix:
        print(' '.join(map(str,row)))

