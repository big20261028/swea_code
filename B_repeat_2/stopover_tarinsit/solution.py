from collections import defaultdict
from heapq import heappush, heappop

# 도시 수
city_n = 0
city_roads = defaultdict(list) # 도시번호 : [(도착번호, 최대중량) .... ]

# st_n에서 각 노드로 이동하는 최단거리 구하기
# 여기서는 각 노드로 이동하는 최대 중량 구하기
def dijkstra(st_n):
    max_weight = [0] * city_n
    max_weight[st_n] = float('inf')

    hq = [(float('-inf'), st_n)]
    while hq:
        weight, n = heappop(hq)
        weight = -weight
        if weight < max_weight[n]:
            continue

        for next_n, next_w in city_roads[n]:
            need_w = min(weight, next_w)
            if need_w > max_weight[next_n]:
                max_weight[next_n] = need_w
                heappush(hq, (-need_w, next_n))

    return max_weight


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
    # print('-----')
    # print('cal 함수 실행')
    city_list = [sCity] + mStopover[:] + [eCity]

    max_weight_paths = []
    for n in city_list:
        max_weight_paths.append(dijkstra(n))

    #print(city_list, M)

    min_weight = float('inf')
    for i in range(M + 1):
        #print(city_list[i], max_weight_paths[i])
        need_weight = max_weight_paths[i][city_list[i+1]]
        if need_weight == 0:
            return -1
        min_weight = min(min_weight, need_weight)
    #print(max_weight_paths)
    #print(min_weight)

    #print('cal 종료')
    #print('-----')
    return min_weight