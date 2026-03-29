from typing import List
from collections import defaultdict
from heapq import heappush, heappop

INF = float('inf')
graph = defaultdict(dict)
comp = defaultdict(dict)
N = 0


def get_group(node):
    return 0 if node <= 3 else node // 3


def is_head_node(node):
    return node <= 3 or node % 100 in (1,2,3)


def group_internal_dijkstra(g):
    reps = [g * 100 + 1, g * 100 + 2, g * 100 + 3,]

    for s in reps:
        for e in reps:
            comp[s].pop(e, None)
            comp[e].pop(s, None)

    for start in reps:
        dist = defaultdict(lambda : INF)
        dist[start] = 0
        pq = [(0, start)]
        while pq:
            d, u = heappop(pq)
            if d > dist[u]: continue
            for v, w in graph[u].items():
                if get_group(v) == g:
                    nd = d + w
                    if nd < dist[v]:
                        dist[v] = nd
                        heappush(pq, (nd, v))
        for end in reps:
            if start != end and dist[end] < INF:
                comp[start][end] = dist[end]
                comp[end][start] = dist[end]

def update_external(u, v, w=None, remove=False):
    if remove:
        comp[u].pop(v, None)
        comp[v].pop(v, None)
    else:
        if w < comp[u].get(v, INF):
            comp[u][v] = comp[v][u] = w


def update_graph(node_a, node_b, mTime=None):
    if mTime is None:
        if node_a not in graph or node_b not in graph[node_a]:
            return
        del graph[node_a][node_b]
        del graph[node_b][node_a]
    else:
        graph[node_a][node_b] = mTime
        graph[node_b][node_a] = mTime

    ga, gb = get_group(node_a), get_group(node_b)
    if ga == gb:
        group_internal_dijkstra(ga)




def init(N : int, K : int, mNodeA : List[int], mNodeB : List[int], mTime : List[int]) -> None:
    pass

def addLine(mNodeA : int, mNodeB : int, mTime : int) -> None:
    pass

def removeLine(mNodeA : int, mNodeB : int) -> None:
    pass

def checkTime(mNodeA : int, mNodeB : int) -> int:
    return 0