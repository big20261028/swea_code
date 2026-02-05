### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
def do_power(n,m):
    if m == 0:
        return 1
    else:
        return n * do_power(n,m-1)

# 테스트 케이스
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    n,m = map(int, input().split())

    result = do_power(n,m)
    print(f"#{test_case} {result}")
