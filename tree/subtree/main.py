import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import deque, defaultdict

class TreeNode:
    def __init__(self,root):
        self.val = root
        self.left = None
        self.right = None

def search(root):
    global cnt
    if root:
        cnt += 1
        search(root.left)
        search(root.right)

T = int(input())
for tc in range(1,T+1):
    E, N = map(int,input().split())
    arr = list(map(int,input().split()))
    queue = deque(arr)
    graph_dict = defaultdict(list)

    node_list = [ TreeNode(i) for i in range(E+2) ]

    while queue:
        parent = queue.popleft()
        child = queue.popleft()
        graph_dict[parent].append(child)

    for node in node_list:
        children = graph_dict[node.val]
        if len(children) >= 1:
            node.left = node_list[children[0]]
        if len(children) >= 2:
            node.right = node_list[children[1]]

    cnt = 0
    search(node_list[N])
    print(f'#{tc} {cnt}')



