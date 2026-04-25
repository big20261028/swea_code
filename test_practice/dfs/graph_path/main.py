import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import defaultdict

T = int(input())

def dfs(node, visited):
    global result

    if node == end_node:
        result = 1
        return

    if result == 1:
        return

    for next_node in graph_paths[node]:
        if next_node in visited:
            continue
        dfs(next_node, visited + [next_node])


for tc in range(1,T+1):
    V, E = map(int,input().split())
    graph_paths = defaultdict(set)
    for _ in range(E):
        start, end = map(int,input().split())
        graph_paths[start].add(end)
    st_node, end_node = map(int,input().split())
    result = 0

    dfs(st_node, list())

    print(f'#{tc} {result}')