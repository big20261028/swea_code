### 제출 전에 지우기 ###
import sys
sys.stdin = open("sample_input.txt", "r")
### 제출 전에 지우기 ###
'''
생각 정리용 공간


'''

class Queue:
    def __init__(self,capacity=10):
        self.rear = 0
        self.front = 0
        self.capacity = capacity+1
        self.queue = [None] * self.capacity

    def is_empty(self):
        return self.rear == self.front

    def is_full(self):
        return (self.rear+1 % self.capacity) == self.front

    def enqueue(self,data):
        if self.is_full():
            raise IndexError('큐가 가득 찼습니다.')
        self.rear = (self.rear+1) % self.capacity
        self.queue[self.rear] = data

    def dequeue(self):
        if self.is_empty():
            raise IndexError('큐가 비었습니다.')
        self.front = (self.front+1) % self.capacity
        result = self.queue[self.front]
        self.queue[self.front] = None
        return result


# 테스트 케이스
T = int(input())
for test_case in range(1, T + 1):
    n,m = map(int,input().split())
    arr = list(map(int, input().split()))

    # from collections import deque
    #
    # queue = deque(arr)
    #
    # for i in range(m):
    #     queue.append(queue.popleft())
    #
    # result = queue.popleft()

    queue = Queue(capacity=n)

    for item in arr:
        queue.enqueue(item)

    for i in range(m):
        data = queue.dequeue()
        queue.enqueue(data)

    result = queue.dequeue()

    print(f"#{test_case} {result}")
