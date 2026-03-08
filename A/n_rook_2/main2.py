N = int(input()) # 세로크기
M = int(input()) # 가로크기
K = int(input()) # 룩의 수

M_set = set([ i for i in range(M)])
N_set = set([ i for i in range(N)])

from collections import defaultdict

visited = [[False] * N for _ in range(M)]
total = 0

def dfs(deps,visited,set_data):
    global total

    if deps == K:
        total += 1
        return

    for i in M_set:
        for j in N_set:

            for si,sj in set_data:
                if i
