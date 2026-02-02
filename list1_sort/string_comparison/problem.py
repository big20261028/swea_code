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
    str1 = input()
    str2 = input()
    # result = None
    # if str1 in str2:
    #     result = 1
    # else :
    #     result = 0


    print(f"#{test_case} {int(str1 in str2)}")
