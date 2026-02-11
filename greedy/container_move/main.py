import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())

for tc in range(1,T+1):
    n,m = map(int,input().split())
    wi = list(map(int,input().split()))
    ti = list(map(int,input().split()))

    used = [0] * n

    wi.sort(reverse=True)
    ti.sort(reverse=True)

    total = 0

    for t in ti:
        for i,w in enumerate(wi):
            if w <= t and used[i] == 0:
                total += w
                used[i] = 1
                # print(total)
                # print(used)
                break

    print(f'#{tc} {total}')
