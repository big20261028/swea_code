import sys
sys.stdin = open('sample_input.txt', 'r')

import heapq

def prim(vertices,edges):
    mst = []

    graph_dict = {v: [] for v in vertices}
    for st_v, end_v, w in edges:
        graph_dict[st_v].append((end_v,w))
        graph_dict[end_v].append((st_v,w))

    visited = set()
    start = vertices[0]
    hq = [[w, start, end] for end,w in graph_dict[start]]
    heapq.heapify(hq)
    visited.add(start)

    while hq:
        w, st, end = heapq.heappop(hq)
        if end in visited: continue

        visited.add(end)
        mst.append((st, end, w))

        for next_e, next_w in graph_dict[end]:
            if next_e in visited: continue
            heapq.heappush(hq, [next_w, end, next_e])
    return mst


T = int(input())

for tc in range(1,T+1):
    # 노드 갯수, 간선 갯수
    V, E = map(int,input().split())
    # 간선이 많음, 프림 알고리즘 사용
    vertices = [ i for i in range(V+1) ]
    # 양끝 노드 n1, n2, 가중치 w
    edges = [ list(map(int,input().split())) for _ in range(E) ]

    result = prim(vertices,edges)

    total_weight = 0

    for item in result:
        total_weight += item[2]

    print(f'#{tc} {total_weight}')

