import sys
sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    matrix = [ list(map(int,input().split())) for _ in range(N)]

    #max_val = float('-inf')
    max_cnt = 0

    for i in range(N):
        for j in range(N):

            for k in range(0,N*2):
                cost = ((k+1)**2) + (k**2)
                profit = 0
                cnt = 0
                for x in range(i-k,i+k+1):
                    for y in range(j-k,j+k+1):

                        if 0<=x<N and 0<=y<N:
                            if abs(x-i) + abs(y-j) <= k:
                                if matrix[x][y] == 1:
                                    profit += M
                                    cnt += 1

                if profit - cost >= 0:
                    max_cnt = max(max_cnt,cnt)

    print(f"#{tc} {max_cnt}")
