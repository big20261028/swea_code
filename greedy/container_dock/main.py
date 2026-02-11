import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    tasks = [ list(map(int,input().split())) for _ in range(n) ]

    tasks.sort(key=lambda x : x[1])

    #print(tasks)

    #start = 0
    end = 0

    cnt = 0
    for s,e in tasks:
        if s < end:
            continue
        else:
            cnt += 1
            end = e

    print(f'#{tc} {cnt}')