import sys
sys.stdin = open('sample_input.txt','r')

class TreeNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, val):
        if self.root is None:
            self.root = TreeNode(val)
        else:
            self._add(self.root, val)

    def _add(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._add(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._add(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _minValueNode(self, node):
        while node.left is not None:
            node = node.left
        return node

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.val:
            node.left = self._delete(node.left, key)
        elif key > node.val:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._minValueNode(node.right)
            node.val = temp.val
            node.right = self._delete(node.right, temp.val)

        return node

class MinHeap:
    def __init__(self):
        self.heap = []

    def heappush(self, item):
        self.heap.append(item)
        self._siftup(len(self.heap) - 1)

    def _siftup(self, idx):
        parent = (idx - 1) // 2
        while idx > 0 and self.heap[idx] < self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx - 1) // 2

    def heappop(self):
        if len(self.heap) == 0:
            raise IndexError('힙이 비었습니다.')
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._siftdown(0)
        return root

    def _siftdown(self, idx):
        n = len(self.heap)
        largest = idx
        left = 2 * idx + 1
        right = 2 * idx + 2

        if left < n and self.heap[left] > self.heap[largest]:
           largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != idx:
            self.heap[idx], self.heap[largest] = self.heap[largest], self.heap[idx]
            self._siftdown(largest)

    def last_node_ancestor(self):
        return self._ancestor_sum(len(self.heap)-1, 0) - self.heap[len(self.heap)-1]

    def _ancestor_sum(self, idx, total=0):
        # 초기값은 가장 마지막 노드의 인덱스값
        # 노드의 조상 노드는 인덱스 //2
        if idx == 0:
            return self.heap[idx]
        total += self._ancestor_sum((idx-1)//2, total) # 5 2 0
        return total + self.heap[idx]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))

    heap = MinHeap()
    for item in arr:
        heap.heappush(item)

    result = heap.last_node_ancestor()
    print(f'#{tc} {result}')