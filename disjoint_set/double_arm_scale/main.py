import sys
sys.stdin = open('sample_input.txt', 'r')

import math

def dfs(deps, l_plate, r_plate, used_w):
    global total

    if l_plate < r_plate:
        return

    if l_plate * 2 >= total_w:
        total += 2 ** (N - deps) * math.factorial(N-deps)
        return

    if deps == N:
        total += 1

    for i in range(len(arr)):
        if used_w[i]: continue
        used_w[i] = True
        dfs(deps + 1, l_plate + arr[i], r_plate, used_w)
        dfs(deps + 1, l_plate, r_plate + arr[i], used_w)
        used_w[i] = False

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = list(map(int,input().split()))
    total_w = sum(arr)
    total = 0

    used_w = [False] * N

    dfs(0, 0, 0, used_w)

    print(f'#{tc} {total}')