import sys
sys.stdin = open('input.txt','r')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]

    dxy = [ (1,0),(-1,0),(0,1),(0,-1) ]

    max_val = 0

    for i in range(N):
        for j in range(M):
            power = matrix[i][j]
            for dx,dy in dxy:
                nx,ny = i,j
                for m in range(matrix[i][j]):
                    nx += dx
                    ny += dy
                    if 0 <= nx < N and 0 <= ny < M:
                        power += matrix[nx][ny]
            max_val = max(max_val,power)

    print(f'#{tc} {max_val}')
