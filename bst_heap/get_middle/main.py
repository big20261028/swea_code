import sys
sys.stdin = open('sample_input.txt', 'r')

from heapq import heappop,heappush

class MaxHeap:
    def __init__(self):
        self.max_hq = []

    def heap_append(self, val):
        self.max_hq.append(val)
        self._siftup(len(self.max_hq)-1)

    def _siftup(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.max_hq[idx] > self.max_hq[parent]:
            self.max_hq[idx], self.max_hq[parent] = self.max_hq[parent], self.max_hq[idx]
            idx = parent
            parent = (idx - 1) // 2

    def heap_pop(self):
        if len(self.max_hq) == 0:
            raise IndexError('힙이 비었습니다.')
        if len(self.max_hq) == 1:
            return self.max_hq.pop()
        root = self.max_hq[0]
        self.max_hq[0] = self.max_hq.pop()
        self._siftdown(0)
        return root

    def _siftdown(self, idx):
        n = len(self.max_hq)
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < n and self.max_hq[left] > self.max_hq[largest]:
            largest = left
        if right < n and self.max_hq[right] > self.max_hq[largest]:
            largest = right
        if largest != idx:
            self.max_hq[idx], self.max_hq[largest] = self.max_hq[largest], self.max_hq[idx]
            self._siftdown(largest)


T = int(input())
for tc in range(1,T+1):
    N, A = map(int,input().strip().split())
    left_heap = MaxHeap()
    left_heap.heap_append(A)
    right_heap = []

    sum_val = 0

    for _ in range(N):
        x,y = map(int,input().strip().split())
        if x > y:
            x, y = y, x
        left_heap.heap_append(x)
        heappush(right_heap, y)
        if left_heap.max_hq[0] > right_heap[0]:
            l_val, r_val = left_heap.heap_pop(), heappop(right_heap)
            left_heap.heap_append(r_val)
            heappush(right_heap, l_val)
        sum_val += left_heap.max_hq[0]

    print(f'#{tc} {sum_val % 20171109}')
    # print(left_heap.max_hq)
    # print(right_heap)
    # print(f'#{tc} {left_heap.max_hq[0]}')

    #matrix = [ list(map(int,input().split())) for _ in range(N) ]
    #print(matrix)
