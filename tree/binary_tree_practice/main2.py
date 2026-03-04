import sys
sys.stdin = open('input.txt','r')

V = int(input())

arr = list(map(int,input().split()))

from collections import deque, defaultdict

graph_dict = defaultdict(list)

queue = deque(arr)

while queue:
    parent = queue.popleft()
    child  = queue.popleft()
    graph_dict[parent].append(child)

class TreeNode:
    def __init__(self,root):
        self.val = root
        self.left = None
        self.right = None

node_list = [ TreeNode(i) for i in range(V+1) ]

for node in node_list:
    children = graph_dict[node.val]
    if len(children) >= 1:
        node.left = node_list[children[0]]
    if len(children) >= 2:
        node.right = node_list[children[1]]

def preorder_traversal(root):
    if root:
        print(root.val, end=' ')
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=' ')

preorder_traversal(node_list[1])
print()
inorder_traversal(node_list[1])
print()
postorder_traversal(node_list[1])
print()
