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
    N = int(input())
    #arr = list(map(int, input().split()))
    stack = []
    for i in range(1,N+1):
        temp_list = []
        if i == 1:
            temp_list.append(1)
        else:
            for n in range(i):
                before_line = stack[i-2]
                num = 0
                if n == 0:
                    num += before_line[n]
                elif n == i-1:
                    num += before_line[n-1]
                else:
                    num += before_line[n-1] + before_line[n]
                temp_list.append(num)
        #print(temp_list)
        stack.append(temp_list)

    print(f"#{test_case}")
    for item in stack:
        print(' '.join(map(str,item)))

    # result = None
    # print(f"#{test_case} {result}")
