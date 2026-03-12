from collections import defaultdict
from heapq import heappush,heappop,heapify

# 시작지 -> 경유지1 -> 경유지2 -> 도착지
# 시작지에서 경유지1로 가는 최대중량 길 구하기

best_load_dict = {}
# 도시의 개수
n = 0
# 도로의 개수
k = 0

spot_load_dict = defaultdict(list)


def dijkstra(st_node):
    print('다익스트라 실행')
    max_weight = [0] * n
    max_weight[st_node] = float('inf')
    hq = [(float('-inf'), st_node)]

    while hq:
        weight, pos = heappop(hq)
        weight = -weight

        if weight < max_weight[pos]:
            continue

        for end_p, end_weight in spot_load_dict[pos]:
            need_weight = min(weight, end_weight)
            #print(spot_load_dict)
            if need_weight > max_weight[end_p]:
                max_weight[end_p] = need_weight
                heappush(hq, (-need_weight, end_p))
    print('다익스트라 종료')
    return list(max_weight)

def init(N, K, sCity, eCity, mLimit):
    print('init 실행')
    global n, k, best_load_dict
    n = N
    k = K
    spot_load_dict = defaultdict(list)

    for i in range(K):
        spot_load_dict[sCity[i]].append((eCity[i], mLimit[i]))
        spot_load_dict[eCity[i]].append((sCity[i], mLimit[i]))
    print('init 종료')

def add(sCity, eCity, mLimit):
    print('add 실행')
    spot_load_dict[sCity].append((eCity, mLimit))
    spot_load_dict[eCity].append((sCity, mLimit))
    print('add 종료')


def calculate(sCity, eCity, M, mStopover):
    print('calculate 실행')
    # 지점 번호
    target_list = [sCity] + mStopover[:] + [eCity]
    min_w = float('inf')

    need_weight_list = []
    for target in target_list:
        need_weight_list.append(dijkstra(target))

    for i in range(M+1):
        need = need_weight_list[i][target_list[i+1]]
        min_w = min(min_w, need)
    print('calculate 종료')
    return min_w