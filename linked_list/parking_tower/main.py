import sys
sys.stdin = open('sample_input.txt','r')

from collections import deque

T = int(input())
for test_case in range(1,T+1):
    n,m = map(int,input().split())

    costs = [ int(input()) for _ in range(n) ]
    weights = [ int(input()) for _ in range(m) ]

    # 주차할 공간
    places = [None] * n
    # 기다리고 있을 차량 데이터 저장
    waiting = deque()

    # print('주차공간: ',places)
    # print('무게별값: ',costs)
    # print('차량번호별 무게: ',weights)

    #print(places)
    total = 0
    for _ in range(m*2):
        # 들어온 차량의 번호 입력
        target = int(input())
        if target > 0 :
            try:
                i = places.index(None)
                places[i] = target
            except Exception as e:
                waiting.append(target)
        elif target < 0 :
            target = abs(target)
            i = places.index(target)
            total += costs[i] * weights[target-1]
            if len(waiting) > 0:
                places[i] = waiting.popleft()
            else:
                places[i] = None

    print(f"#{test_case} {total}")
