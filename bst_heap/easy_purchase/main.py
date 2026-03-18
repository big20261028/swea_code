import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())

    cashes = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    counts = [0] * 8

    for i in range(8):
        counts[i] += N // cashes[i]
        N = N % cashes[i]

    print(f'#{tc}')
    print(f'{" ".join(map(str,counts))}')
