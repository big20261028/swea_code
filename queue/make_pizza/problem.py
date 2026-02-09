### 제출 전에 지우기 ###
import sys
sys.stdin = open("sample_input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
from collections import deque
# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n,m = int(input())
    arr = list(map(int, input().split()))
    oven = [None]*n

    pizza_queue = deque(arr)
    queue = deque(oven)

    cnt = 0
    while cnt < m-1:
        cnt = 1
        check = queue.popleft()
        if check//2 == 0:
            cnt += 1

        if check == None and len(pizza_queue) > 0:
            queue.append(pizza_queue.popleft())




    result = None
    print(f"#{test_case} {result}")
