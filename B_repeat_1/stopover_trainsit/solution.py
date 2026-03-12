from collections import defaultdict
from heapq import heappush, heappop

city_n = 0
# 출발도시번호 : [ (도착도시번호, 중량)..... ]
city_roads = defaultdict(list)

def dijkstra(st_n):
    result_list = [float('-inf')] * city_n
    result_list[st_n] = 0
    hq = [(float('-inf'), st_n)]

    while hq:
        weight, pos = heappop(hq)
        weight = -weight
        if weight < result_list[pos]:
            continue

        for next_n, next_w in city_roads[pos]:
            need_weight = min(next_w, weight)
            if need_weight > result_list[next_n]:
                result_list[next_n] = need_weight
                heappush(hq, (-need_weight, next_n))
    return result_list

def init(N, K, sCity, eCity, mLimit):
    global city_n, city_roads
    city_n = N
    city_roads = defaultdict(list)

    for i in range(K):
        city_roads[sCity[i]].append((eCity[i], mLimit[i]))
        city_roads[eCity[i]].append((sCity[i], mLimit[i]))


def add(sCity, eCity, mLimit):
    city_roads[sCity].append((eCity, mLimit))
    city_roads[eCity].append((sCity, mLimit))


def calculate(sCity, eCity, M, mStopover):
    city_num_list = [sCity] + mStopover[:] + [eCity]

    max_weights_paths = []
    for city_n in city_num_list:
        max_weights_paths.append(dijkstra(city_n))

    max_weight = float('inf')
    for i in range(M+1):
        need_weight = max_weights_paths[i][city_num_list[i+1]]
        if need_weight == float('-inf'):
            return -1
        max_weight = min(max_weight, need_weight)

    return max_weight