### 제출 전에 지우기 ###
import sys
sys.stdin = open("GNS_test_input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n, test_n = input().split()

    word_list = [ "ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN" ]

    new_list = []
    arr = list(input().split())
    for char in arr:
        new_list.append(word_list.index(char))

    new_list.sort()
    result = ''
    for i in new_list:
        result += word_list[i] + " "

    print(f"#{test_case}\n{result}")
