import sys
sys.stdin = open('input.txt', 'r')

from collections import defaultdict
from heapq import heappush, heappop

def dijkstra(st_node):
    short_paths = [float('inf')] * N
    short_paths[st_node] = 0
    hq = [(0, st_node)]
    while hq:
        t, node = heappop(hq)
        if t > short_paths[node]:
            continue
        for next_t, next_node in path_info[node]:
            need_t = next_t + t
            if need_t < short_paths[next_node]:
                short_paths[next_node] = need_t
                heappush(hq, (need_t, next_node))

    return short_paths


T = int(input())
for tc in range(1, T + 1):
    N, M, X = map(int, input().split())
    path_info = defaultdict(list)
    for _ in range(M):
        x, y, c = map(int, input().split())
        path_info[x-1].append((c, y-1))

    short_paths = dijkstra(X - 1)
    print(short_paths)
    #short_paths[X-1]  = float('inf')

    print(f'#{tc} {max(short_paths)}')