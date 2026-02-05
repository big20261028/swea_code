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
    #N = int(input())
    text = input()

    i = 0
    while i < len(text)-1:
        if len(text) < 2:
            break
        if text[i] == text[i+1]:
            if len(text) > i+2:
                text = text[:i] + text[i+2:]
            else:
                text = text[:i]
            i = 0
        else:
            i += 1


    #print(text)
    result = len(text)
    print(f"#{test_case} {result}")
