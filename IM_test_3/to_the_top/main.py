import sys
sys.stdin = open('1_sample_input.txt','r')

T = int(input())

for tc in range(1,T+1):
    # 선택기회, 폭탄 설치 층
    N,P = map(int,input().split())
    # 팩토리얼 문제
    # 1 ~ N 번 선택,
    # 각 팩토리얼 값 확인, 만약 겹치면 1 빼기

    total = 0
    for i in range(1,N+1):
        total += i
        if total == P:
            total -= 1

    print(f'{total}')