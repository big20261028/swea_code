import sys
sys.stdin = open('carrot_sample_in.txt','r')

T = int(input())
for test_case in range(1, T+1):
    n = int(input())
    carrots = list(map(int,input().split()))

    max_cnt = 0
    cnt = 1
    for i in range(1,len(carrots)):
        if carrots[i-1] < carrots[i]:
            cnt += 1
        else:
            if max_cnt < cnt :
                max_cnt = cnt
            cnt = 1
    if max_cnt < cnt:
        max_cnt = cnt

    print(f'#{test_case} {max_cnt}')