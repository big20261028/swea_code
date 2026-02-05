### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
#def calculate(text):



# 테스트 케이스
T = 10
for test_case in range(1, T + 1):
    N = int(input())
    text = input()
    operator_dict = { '+' : 1 }
    stack = []
    result = ''
    for char in text:
        if char.isnumeric():
            result += char
            continue
        if stack and stack[-1] == char:
            result += stack.pop()
        stack.append(char)
    #print(len(stack))
    result += ''.join(map(str,stack))
    #print(result)

    stack = []
    #result = ''
    for char in result:
        #print(stack)
        if char.isnumeric():
            stack.append(char)
            continue
        if char == '+':
            o2 = int(stack.pop())
            o1 = int(stack.pop())
            stack.append(o1+o2)
    # print(stack)
    result = stack.pop()


    #result = None
    print(f"#{test_case} {result}")
