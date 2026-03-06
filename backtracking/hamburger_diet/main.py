import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(deps, t_sum, t_cal):
    global max_val

    if t_cal > L:
        return
    if deps == N:
        max_val = max(max_val,t_sum)
        return

    dfs(deps+1, t_sum + arr[deps][0], t_cal + arr[deps][1])
    dfs(deps+1, t_sum, t_cal)

T = int(input())
for tc in range(1, T+1):
    N, L = map(int,input().strip().split())
    # 점수, 칼로리
    arr = [ list(map(int,input().split())) for _ in range(N) ]
    max_val = 0
    dfs(0,0,0)

    print(f'#{tc} {max_val}')