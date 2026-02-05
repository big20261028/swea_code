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
    #N = int(input())
    word = input()

    result = 1

    for i in range(len(word)//2):
        j = len(word) - 1 - i
        if word[i] != word[j]:
            result = 0
            break


    print(f"#{test_case} {result}")
