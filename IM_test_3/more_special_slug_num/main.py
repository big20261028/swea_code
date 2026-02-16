import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [ [0]*N for _ in range(N) ]

    matrix[0][0] = 1
    matrix[0][1] = 2

    # 아래 대각선, 위 대각선
    dxy = [(1,-1),(-1,1)]
    dr = 0
    x,y = 0,1
    for i in range(3,(N**2)+1):
        dx,dy = dxy[dr]
        nx,ny = x+dx, y+dy
        # 아래 대각선 이동중일때
        if dr==0:
            # 만약 벽에 부딛혔다면
            if not (0<=nx<N and 0<=ny<N):
                # 아래에 자리가 있다면
                if 0 <= x+1 < N:
                    #아래로 한칸 이동
                    nx,ny = x+1,y
                # 아래에 자리가 없다면
                else:
                    # 오른쪽으로 한칸 이동
                    nx,ny = x,y+1
                dr = 1
            x,y = nx,ny
        # 위 대각선 이동중일때
        elif dr==1:
            # 벽에 부딛혔고
            if not (0 <= nx < N and 0 <= ny < N):
                # 오른쪽에 자리가 있다면
                if 0<= y+1 < N:
                    # 오른쪽으로 한칸 이동 후 방향 아래 대각선으로 변경
                    nx,ny = x,y+1
                # 오른쪽에 자리가 없다면
                else:
                    # 아래로 한칸 이동 후 방향 변경
                    nx,ny = x+1,y
                dr = 0
            x,y = nx,ny
        matrix[x][y] = i

    print(f'#{tc}')
    for row in matrix:
        print(' '.join(map(str,row)))