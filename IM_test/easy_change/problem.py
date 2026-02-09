### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    moneys = (50000,10000,5000,1000,500,100,50,10)
    counts = [0,0,0,0,0,0,0,0]

    # print(len(moneys))
    # print(len(counts))

    for i,m in enumerate(moneys):
        counts[i] = n//m
        n = n%m

    print(f"#{test_case}")
    print(' '.join(map(str,counts)))






    # result = None
    # print(f"#{test_case} {result}")
