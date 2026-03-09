import sys
sys.stdin = open('re_sample_input.txt', 'r')

from collections import defaultdict
import math, heapq

def prim(vertices,edges):

    mst = []

    visited = set()
    start = vertices[0]
    min_path = [ (w, start, end) for end, w in edges[start] ]
    heapq.heapify(min_path)
    visited.add(start)

    while min_path:
        w, st, end = heapq.heappop(min_path)
        if end in visited: continue

        visited.add(end)
        mst.append((w, st, end))

        for next_e, next_w in edges[end]:
            if next_e in visited: continue
            heapq.heappush(min_path, (next_w, end, next_e))
    return mst

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    X = list(map(int,input().split()))
    Y = list(map(int,input().split()))
    E = float(input())

    # 각 섬 사이의 (길이 * 환경부담금) 을 가중치로 하는 edges 구하기
    edges = defaultdict(list)

    for i in range(N):
        x,y = X[i], Y[i]
        for t_i in range(N):
            if t_i == i: continue
            t_x, t_y = X[t_i], Y[t_i]
            dist = (x - t_x)**2 + (y - t_y)**2
            #price = dist * E
            edges[i].append((t_i, dist))

    #print(edges)
    vertices = list(range(N))

    result = prim(vertices, edges)

    total = sum(item[0] for item in result)
    total = int((total * E) + 0.5)
    total = int(total)

    print(f'#{tc} {total}')
