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
    n,m = map(int,input().split())
    arr = list(map(int, input().split()))

    new_arr = zip(arr,range(m))

    oven = [None]*n

    pizza_queue = deque(new_arr)
    queue = deque(oven)

    cnt = len(arr)
    last_pizza = 0
    while cnt > 0:
        check = queue.popleft()

        if check == None and len(pizza_queue) > 0:
            queue.append(pizza_queue.popleft())
            continue

        cheeze, last_pizza = check

        cheeze //= 2

        if cheeze == 0:
            cnt -= 1
            if len(pizza_queue) > 0:
                queue.append(pizza_queue.popleft())
        else:
            queue.append((cheeze,last_pizza))

    result = last_pizza + 1
    print(f"#{test_case} {result}")
