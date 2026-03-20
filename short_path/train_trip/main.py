import sys
sys.stdin = open('sample_input.txt', 'r')
from collections import defaultdict
from heapq import heappop, heappush

def dijkstra(st_node):
    short_paths = [float('inf')] * N
    short_paths[st_node] = 0
    hq = [(0, st_node)]
    while hq:
        cost, node = heappop(hq)
        if cost > short_paths[node]:
            continue
        for next_c, next_node in path_info[node]:
            need_cost = next_c + cost
            if need_cost < short_paths[next_node]:
                short_paths[next_node] = need_cost
                heappush(hq, (need_cost, next_node))

    return short_paths


Case = int(input())

for tc in range(1, Case+1):
    N, T = map(int, input().split())
    path_info = defaultdict(list)
    for _ in range(T):
        a, b, w = map(int, input().split())
        path_info[a].append((w, b)) # 단방향 그래프
        #path_info[b].append((w, a))

    short_paths = dijkstra(0)
    result = short_paths[N-1]
    if result == float('inf'):
        result = 'impossible'
    print(f'#{tc} {result}')