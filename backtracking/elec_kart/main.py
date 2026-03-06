import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(deps,cur_pos,usage,visited):
    global min_val

    if usage > min_val:
        return

    if deps == N-1:
        usage += matrix[cur_pos][0]
        min_val = min(min_val, usage)
        return

    for j in range(N):
        if j == cur_pos: continue
        if visited[j]: continue
        visited[j] = True
        dfs(deps+1, j, usage + matrix[cur_pos][j],visited)
        visited[j] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int,input().split())) for _ in range(N)]

    min_val = float('inf')
    visited = [False] * N
    visited[0] = True
    dfs(0,0,0,visited)

    print(f'#{tc} {min_val}')