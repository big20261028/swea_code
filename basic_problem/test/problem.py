### 제출 전에 지우기 ###
import sys
sys.stdin = open("s_input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
from collections import defaultdict
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    bus_load = [ list(map(int,input().split())) for _ in range(N)]
    p = int(input())
    bus_stop = [ int(input()) for _ in range(p) ]

    # 지나간 정류장 데이터를 딕셔너리로 관리하기
    visit_dict = defaultdict(int)
    for a,b in bus_load:
        # i번째 버스 노선은 번호가 Ai이상이고,Bi이하인 모든 정류장
        for i in range(a,b+1):
            visit_dict[i] += 1

    result = ""
    for target in bus_stop:
        result += str(visit_dict[target]) + " "
    print(f"#{test_case} {result}")
