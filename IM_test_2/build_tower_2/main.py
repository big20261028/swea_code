import sys
sys.stdin = open('input6_sample.txt','r')

T = int(input())
for tc in range(1, T+1):
    N,M = map(int,input().split())
    towers = [list(map(int,input().split())) for _ in range(M)]
    boxs = list(map(int,input().split()))

    boxs.sort(reverse=True)

    tower_h = [1] * M

    total = 0

    for box in boxs:
        val = float('inf')
        idx = -1
        for i in range(M):
            if towers[i][0] < tower_h[i]: continue
            p = box * towers[i][1] * tower_h[i]
            if p < val:
                val = p
                idx = i
        total += val
        tower_h[idx] += 1

    print(f'#{tc} {total}')



