import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(deps,val):
    global total

    if val == K:
        total += 1
        return

    if val > K or deps == N:
        return

    dfs(deps+1, val + arr[deps])
    dfs(deps+1, val)

T = int(input())
for tc in range(1,T+1):
    N, K = map(int, input().strip().split())
    arr = list(map(int, input().split()))

    total = 0
    dfs(0,0)

    print(f'#{tc} {total}')