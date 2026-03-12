from collections import defaultdict
from heapq import heappush, heappop, heapify

city_n = 0
road_n = 0
# 도시번호 : [ (도착도시 번호, 최대중량) .... ]
city_roads = defaultdict(list)

def dijkstra(st_n):
    max_weight_list = [-1] * city_n
    max_weight_list[st_n] = float('inf')

    hq = [ (float('-inf'), st_n)]
    while hq:
        weight, pos = heappop(hq)
        weight = -weight
        if weight < max_weight_list[pos]:
            continue

        for next_pos, next_w in city_roads[pos]:
            need_weight = min(next_w, weight)
            if need_weight > max_weight_list[next_pos]:
                max_weight_list[next_pos] = need_weight
                heappush(hq, (-need_weight, next_pos))
    return max_weight_list

def init(N, K, sCity, eCity, mLimit):
    global city_n, road_n, city_roads
    city_n = N
    road_n = K
    city_roads = defaultdict(list)

    for i in range(K):
        city_roads[sCity[i]].append((eCity[i], mLimit[i]))
        city_roads[eCity[i]].append((sCity[i], mLimit[i]))


def add(sCity, eCity, mLimit):
    city_roads[sCity].append((eCity, mLimit))
    city_roads[eCity].append((sCity, mLimit))


def calculate(sCity, eCity, M, mStopover):
    city_list = [sCity] + mStopover[:] + [eCity]
    max_path_list = []
    for pos in city_list:
        max_path_list.append(dijkstra(pos))
    # print(max_path_list)
    # print(city_list)
    max_weight = float('inf')
    for i in range(M+1):
        need_weight = max_path_list[i][city_list[i+1]]
        # print(need_weight)
        if need_weight == -1:
            return -1
        max_weight = min(need_weight, max_weight)

    return max_weight