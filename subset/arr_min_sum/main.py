import sys
sys.stdin = open('sample_input.txt','r')

def dfs(deps,visited,temp_list):
    global min_val

    if sum(temp_list) >= min_val: return
    if deps == N:
        min_val = min(min_val,sum(temp_list))
        return

    for i in range(N):
        if visited[i]: continue
        visited[i] = True
        dfs(deps+1,visited,temp_list+[matrix[deps][i]])
        visited[i] = False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    matrix = [ list(map(int,input().split())) for _ in range(N) ]
    min_val = float('inf')
    dfs(0,[False]*N,[])
    print(f'#{tc} {min_val}')