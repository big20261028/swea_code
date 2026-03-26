from collections import defaultdict
from heapq import heappush, heappop

city_n = 0
city_roads = defaultdict(list) # city_roads[node] = [ (limit, next_node), (limit, next_node)...]


def dijkstra(st_node):
    max_weights = [float('-inf')] * city_n
    max_weights[st_node] = float('inf')
    hq = [(float('-inf'), st_node)]
    while hq:
        weight, node = heappop(hq)
        weight = -weight
        if weight < max_weights[node]:
            continue

        for next_w, next_node in city_roads[node]:
            need_weight = min(next_w, weight)
            if need_weight > max_weights[next_node]:
                max_weights[next_node] = need_weight
                heappush(hq, (-need_weight, next_node))
    return max_weights


def init(N, K, sCity, eCity, mLimit):
    global city_n, city_roads
    city_n = N
    city_roads = defaultdict(list)
    for i in range(K):
        city_roads[sCity[i]].append((mLimit[i], eCity[i]))
        city_roads[eCity[i]].append((mLimit[i], sCity[i]))


def add(sCity, eCity, mLimit):
    city_roads[sCity].append((mLimit, eCity))
    city_roads[eCity].append((mLimit, sCity))


def calculate(sCity, eCity, M, mStopover):
    target_node_list = [sCity] + mStopover + [eCity]

    max_weights_dict = {}
    for target_node in target_node_list:
        max_weights_dict[target_node] = dijkstra(target_node)
    #print(max_weights_dict)

    result = float('inf')

    for i in range(M+1):
        st_node = target_node_list[i]
        end_node = target_node_list[i+1]

        max_weight = max_weights_dict[st_node][end_node]
        if max_weight == float('-inf'):
            result = float('inf')
            break
        result = min(result, max_weight)


    if result == float('inf'):
        return -1
    else:
        return result