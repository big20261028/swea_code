import sys
sys.stdin = open('sample_input.txt','r')

def dfs(st,end):
    global flag
    if st == end:
        flag = 1
    if flag == 1:
        return
    if st in node_paths:
        for item in node_paths[st]:
            dfs(item,end)

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split())

    node_paths = {}
    for _ in range(E):
        st_node,end_node = map(int,input().split())
        if st_node in node_paths:
            node_paths[st_node].append(end_node)
        else:
            node_paths[st_node] = [end_node]

    st_pos,end_pos = map(int,input().split())

    flag = 0
    dfs(st_pos,end_pos)

    print(f"#{tc} {flag}")

