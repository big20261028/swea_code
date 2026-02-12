import sys
sys.stdin = open('s_input.txt','r')

T = int(input())
for tc in range(1,T+1):
    d,a,b,f = map(int,input().split())

    # 기차가 충돌하는데 걸리는 시간 구하기.
    # 그 시간을 파리의 속력에 곱하기
    t = d / (a+b)
    result = f*t

    print(f'#{tc} {result:.10f}')