import sys
sys.stdin = open('sample_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    n = int(input())
    cnt = 0
    for i in range(-n,n+1):
        for j in range(-n,n+1):
            # 마름모일 경우의 조건
            # if abs(i) + abs(j) <= n:
            #     cnt += 1

            # x^2 + y^2 = z^2
            # 삼각함수 사용
            if i**2 + j**2 <= n**2:

    print(f'#{n} {cnt}')