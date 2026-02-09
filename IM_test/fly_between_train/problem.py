### 제출 전에 지우기 ###
import sys
sys.stdin = open("s_input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    #N = int(input())
    d, a, b, f = map(int,input().split())

    # 충돌하는데 걸린 시간을 구한다
    # 그 시간에 f를 곱하면 끝

    t = d/(a+b)
    result = t*f



    print(f"#{test_case} {result}")
