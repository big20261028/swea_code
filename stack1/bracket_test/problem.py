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
    target = input()

    #top = -1
    stack = []
    # start_bracket = [ '(', '{', '[' ]
    # end_bracket = [ ')', '}', ']' ]
    bracket_dict = {
        ')' : '(',
        '}' : '{',
        ']' : '['
    }

    result = 1
    for char in target:
        #print(stack)
        if char in bracket_dict.values():
            stack.append(char)
        if char in bracket_dict.keys():
            if not stack:
                result = 0
                break
            if stack[-1] != bracket_dict[char]:
                result = 0
                break
            stack.pop()
    #print(target)
    if len(stack) != 0:
        result = 0

    print(f"#{test_case} {result}")
