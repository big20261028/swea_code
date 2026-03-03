import sys
sys.stdin = open('input.txt','r')

V = int(input())

from collections import deque,defaultdict

arr = list(map(int,input().split()))

dict_data = defaultdict(list)
queue_data = deque(arr)

while queue_data:
    parent = queue_data.popleft()
    child = queue_data.popleft()
    dict_data[parent].append(child)

#print(dict_data)

class TreeNode:
    def __init__(self,node):
        self.val = node
        self.left = None
        self.right = None

nodes = {i: TreeNode(i) for i in range(1, V + 1)}

for parent, children_vals in dict_data.items():
    if len(children_vals) >= 1:
        nodes[parent].left = nodes[children_vals[0]]
    if len(children_vals) >= 2:
        nodes[parent].right = nodes[children_vals[1]]

def preorder_traversal(root,result):
    if root:
        result.append(root.val)
        preorder_traversal(root.left,result)
        preorder_traversal(root.right,result)
def inorder_traversal(root,result):
    if root:
        inorder_traversal(root.left,result)
        result.append(root.val)
        inorder_traversal(root.right,result)
def postorder_traversal(root,result):
    if root:
        postorder_traversal(root.left,result)
        postorder_traversal(root.right,result)
        result.append(root.val)

result = []
preorder_traversal(nodes[1],result)
print(' '.join(map(str,result)))
result = []
inorder_traversal(nodes[1],result)
print(' '.join(map(str,result)))
result = []
postorder_traversal(nodes[1],result)
print(' '.join(map(str,result)))