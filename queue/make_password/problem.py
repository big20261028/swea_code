### 제출 전에 지우기 ###
import sys
sys.stdin = open("input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''
from collections import deque

# 테스트 케이스
T = 10
for test_case in range(1, T + 1):
    t = int(input())
    arr = list(map(int, input().split()))

    queue = deque(arr)

    minus = 0
    while True:
        front_data = queue.popleft()-(minus%5 + 1)
        minus += 1
        if front_data<=0:
            queue.append(0)
            break
        queue.append(front_data)

    result = ' '.join(map(str,queue))
    print(f"#{test_case} {result}")
