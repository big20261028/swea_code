import sys
sys.stdin = open('input11_sample.txt','r')

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    max_len = 0
    last_dr = ''
    cnt = 1
    for i in range(N-1):
        if arr[i] < arr[i+1]:
            if last_dr == 'W':
                cnt += 1
            else:
                cnt = 2
            last_dr = 'W'
        elif arr[i] > arr[i+1]:
            if last_dr == 'D':
                cnt += 1
            else:
                cnt = 2
            last_dr = 'D'
        else:
            cnt = 1
            last_dr = ''
        max_len = max(max_len,cnt)
    print(f'#{tc} {max_len}')


    #print(f'#{tc} {max_len}')

