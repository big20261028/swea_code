### 제출 전에 지우기 ###
import sys
sys.stdin = open("sample_input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    cnt = 0
    for x in range(-N,N+1):
        for y in range(-N,N+1):
            if (x**2) + (y**2) <= N**2:
                cnt += 1

    result = cnt
    print(f"#{test_case} {result}")
