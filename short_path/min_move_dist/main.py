import sys
sys.stdin = open('sample_input.txt', 'r')

from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(st_node):
    short_paths = [float('inf')] * (N + 1)
    short_paths[st_node] = 0
    hq = [(0, st_node)]
    while hq:
        dist, node = heappop(hq)
        if dist > short_paths[node]:
            continue
        for next_dist, next_node in path_info[node]:
            need_dist = next_dist + dist
            if need_dist < short_paths[next_node]:
                short_paths[next_node] = need_dist
                heappush(hq, (need_dist, next_node))

    return short_paths

T = int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    path_info = defaultdict(list)
    for _ in range(E):
        s, e, w = map(int, input().split())
        path_info[s].append((w, e))

    short_paths = dijkstra(0)

    print(f'#{tc} {short_paths[N]}')