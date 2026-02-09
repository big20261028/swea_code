### 제출 전에 지우기 ###
import sys
sys.stdin = open("in.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = list(map(int, input().split()))


    result = None
    print(f"#{test_case} {result}")
