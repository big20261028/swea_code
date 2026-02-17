import sys
sys.stdin = open('input7_sample.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    counts = [0]*N

    i = 0
    while i<N-1:
        while counts[i] % 2 == 1 and i != 0:
            target_idx = arr[i] -1
            i = target_idx
            counts[i] += 1
        i += 1
        counts[i] += 1
    print(f'#{tc} {sum((counts))}')

