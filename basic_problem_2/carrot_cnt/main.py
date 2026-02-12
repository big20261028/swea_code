import sys
sys.stdin = open('carrot_sample_in.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    carrots = list(map(int,input().split()))

    cnt = 1
    max_val = 0
    for i in range(N-1):
        if carrots[i] < carrots[i+1]:
            cnt += 1
        else:
            if max_val < cnt:
                max_val = cnt
            cnt = 1

    if max_val < cnt:
        max_val = cnt

    print(f'#{tc} {max_val}')