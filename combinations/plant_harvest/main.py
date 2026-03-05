import sys
sys.stdin = open('input.txt','r')


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [ list(map(int,input())) for _ in range(N) ]

    #print(matrix)

    radius = N // 2

    center_pos = (radius,radius)

    total = 0
    for i in range(N):
        for j in range(N):
            if abs(i-radius) + abs(j-radius) > radius: continue
            total += matrix[i][j]

    print(f'#{tc} {total}')
