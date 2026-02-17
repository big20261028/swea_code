import sys
sys.stdin = open('input4_sample.txt','r')

T = int(input())
for tc in range(1,T+1):
    N,M,K = map(int,input().split())
    answers = list(map(int,input().split()))

    students = [list(map(int,input().split())) for _ in range(N)]

    max_val = float('-inf')
    for student in students:
        cnt = 0
        score = 0
        for i in range(M):
            if answers[i] == student[i]:
                cnt += 1
                if cnt == K:
                    score += 50
                    cnt = 0
                else:
                    score += 10
            else:
                cnt = 0
        max_val = max(max_val,score)

    print(f'#{tc} {max_val}')

