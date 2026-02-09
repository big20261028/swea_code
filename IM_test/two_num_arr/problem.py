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
    n,m = map(int,input().split())
    aj = list(map(int, input().split()))
    bj = list(map(int, input().split()))


    max_val = 0
    for s in range(abs(len(bj)-len(aj))+1):
        sum_val = 0
        end_point = 0
        if len(aj) < len(bj):
            for ia,ib in enumerate(range(s,s+len(aj))):
                #print(ia,ib)
                sum_val += aj[ia] * bj[ib]
            if max_val < sum_val:
                max_val = sum_val
        elif len(aj) > len(bj):

            for ib, ia in enumerate(range(s, s + len(bj))):
                # print(ia,ib)
                sum_val += aj[ia] * bj[ib]
            if max_val < sum_val:
                max_val = sum_val

    result = max_val
    print(f"#{test_case} {result}")
