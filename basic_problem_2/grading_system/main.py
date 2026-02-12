import sys
sys.stdin = open('input3_sample.txt','r')

T = int(input())
for tc in range(1,T+1):
    n,m = map(int,input().split())
    collects = list(map(int,input().split()))
    answers = [list(map(int,input().split())) for _ in range(n)]

    totals = []
    for answer in answers:
        score = 1
        temp = 0
        for i in range(m):
            #print(answer[i], collects[i])
            if answer[i] == collects[i]:
                temp += score
                score += 1
            else:
                score = 1
        totals.append(temp)
        #print('-')

    # print(total)

    result = max(totals) - min(totals)
    print(f'#{tc} {result}')
