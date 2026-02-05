### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = 10
for test_case in range(1, T + 1):
    n = int(input())
    matrix = [ list(input()) for _ in range(8)]

    target_list = list(zip(*matrix))
    target_list.extend(matrix)
    #print(target_list)

    cnt = 0
    for item in target_list:
        for i in range(8-n+1):
            text = item[i:i+n]
            if text == text[::-1]:
                cnt += 1

    result = cnt
    print(f"#{test_case} {result}")
