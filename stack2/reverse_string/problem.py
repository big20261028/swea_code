### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간
'''
# 테스트 케이스
def reverse_str(text):
    #print(text)
    if len(text) == 1:
        return text
    new_text = text[:len(text)-1]
    return ''+text[len(text)-1]+reverse_str(new_text)

T = int(input())
for test_case in range(1, T + 1):
    text = input()
    result =reverse_str(text)
    print(f"{result}")
