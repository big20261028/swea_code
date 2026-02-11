import sys
sys.stdin = open('Sample_input.txt','r')

T = int(input())

for test_case in range(1,T+1):
    n = int(input())
    trees = list(map(int,input().split()))

    # 가장 큰 나무의 크기
    max_h = max(trees)

    # 홀수일에 물주기가 필요한 날의 개수 구하기
    # 필요한 나무 길이
    odd_days = 0
    total_need = 0

    for tree in trees:
        need_h = max_h - tree
        total_need += need_h
        if need_h%2 == 1:
            odd_days += 1

    # 필요한 길이만큼 성장시키기 위한 가장 이상적인 상황 산출
    # 필요한 일수, 한번 물주는 경우, 두번 물주는 경우
    days = (total_need//3) * 2 + total_need%3
    one_water = days//2 + days%2
    two_water = days//2

    # 최소한의 홀수일 물주기가 필요한 날보다, 이상적인 상황에서의 두번 물주는 경우가 적은경우
    # 최소한의 물주기 일자를 확보하기 위해 odd_days를 사용해 필요 일자를 출력한다.
    # 홀수일 물주기가 작거나 같은경우는 그대로 days 출력

    if odd_days <= one_water:
        print(f"#{test_case} {days}")
    else:
        print(f"#{test_case} {(odd_days * 2) - 1}")