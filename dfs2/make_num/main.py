import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import deque

def dfs(num_queue):
    global min_val, max_val
    if len(num_queue) <= 1:
        min_val = min(min_val,num_queue[0])
        max_val = max(max_val,num_queue[0])
        return

    for i in range(4):
        if op_arr[i] <= 0: continue

        oper = oper_list[i]
        op_arr[i] -= 1
        num_1 = num_queue.popleft()
        num_2 = num_queue.popleft()

        if oper == '+':
            num_queue.appendleft( num_1 + num_2 )
            dfs(num_queue)
        elif oper == '-':
            num_queue.appendleft( num_1 - num_2 )
            dfs(num_queue)
        elif oper == '*':
            num_queue.appendleft( num_1 * num_2 )
            dfs(num_queue)
        elif oper == '/':
            num_queue.appendleft( int(num_1 / num_2) )
            dfs(num_queue)

        num_queue.popleft()
        num_queue.appendleft(num_2)
        num_queue.appendleft(num_1)
        op_arr[i] += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    op_arr = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    queue = deque(numbers)

    oper_list = ['+', '-', '*', '/']
    min_val = float('inf')
    max_val = float('-inf')

    dfs(queue)

    print(f'#{tc} {max_val - min_val}')