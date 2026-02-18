import sys
sys.stdin = open('sample_input.txt','r')

from collections import deque

def make_max_val(oper_arr,nums):
    global max_val,min_val
    if oper_arr.count(0) == 4:
        max_val = max(max_val,nums[0])
        min_val = min(min_val,nums[0])
        return
        pass

    for i in range(4):
        if oper_arr[i] == 0: continue

        oper_arr[i] -= 1
        oper = oper_list[i]
        a_num = nums.popleft()
        b_num = nums.popleft()
        if oper == '+':
            nums.appendleft(a_num + b_num)
        elif oper == '-':
            nums.appendleft(a_num - b_num)
        elif oper == '*':
            nums.appendleft(a_num * b_num)
        elif oper == '/':
            nums.appendleft(int(a_num / b_num))

        make_max_val(oper_arr, nums)
        nums.popleft()
        nums.appendleft(b_num)
        nums.appendleft(a_num)
        oper_arr[i] += 1

T = int(input())
#T = 1
for tc in range(1,T+1):
    N = int(input())
    oper_arr = list(map(int,input().split()))
    numbers = list(map(int,input().split()))

    queue = deque(numbers)
    #queue.popleft()

    oper_list = [ '+','-','*','/' ]

    max_val = float('-inf')
    min_val = float('inf')

    make_max_val(oper_arr,queue)

    result = max_val - min_val

    print(f'#{tc} {result}')