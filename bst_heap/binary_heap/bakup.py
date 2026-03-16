import sys
sys.stdin = open('sample_input.txt', 'r')

class TreeNode:
    def __init__(self,node):
        self.key = node
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def search(self, key):
        return self._search(self.root, key)
        pass

    def _search(self, node, key):
        if node == None or node.key == key:
            return node

        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def insert(self, key):
        if self.root == None:
            self.root = key
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left == None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key)
        elif key > node.key:
            if node.right == None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def delete(self, key):
        self._delete(self.root, key)

    def _minValueNode(self,node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def _delete(self, node, key):
        if node == None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._minValueNode(node.right)
            node.key = temp.key
            node.right = self._delete(node.right, temp.key)

        return node


T = int(input())
for tc in range(1,T+1):
    N = int(input())

    arr = list(map(int,input().split()))

