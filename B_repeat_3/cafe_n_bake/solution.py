from collections import defaultdict
from heapq import heappop, heappush

building_n = 0
building_loads = defaultdict(list) # 건물번호 = [ (도로 길이, 다음건물), (도로 길이, 다음건물), ... ]

# 해당 건물 번호 리스트에서 각 지점까지의 최소 거리 구하기
def multi_dijkstra(target_list, R):
    min_dist_list = [float('inf')] * building_n
    hq = []
    for node in target_list:
        min_dist_list[node] = 0
        heappush(hq, (0, node))

    while hq:
        dist, node = heappop(hq)
        if dist > min_dist_list[node]:
            continue
        if dist > R:
            continue

        for next_dist, next_node in building_loads[node]:
            need_dist = next_dist + dist
            if need_dist < min_dist_list[next_node]:
                min_dist_list[next_node] = need_dist
                if need_dist <= R:
                    heappush(hq, (need_dist, next_node))

    return min_dist_list




def init(N, K, sBuilding, eBuilding, mDistance):
    global building_n, building_loads
    building_n = N
    building_loads = defaultdict(list)
    for i in range(K):
        building_loads[sBuilding[i]].append((mDistance[i], eBuilding[i]))
        building_loads[eBuilding[i]].append((mDistance[i], sBuilding[i]))


def add(sBuilding, eBuilding, mDistance):
    building_loads[sBuilding].append((mDistance, eBuilding))
    building_loads[eBuilding].append((mDistance, sBuilding))


def calculate(M, mCoffee, P, mBakery, R):
    cafe_min_dist_list = multi_dijkstra(mCoffee, R)
    bake_min_dist_list = multi_dijkstra(mBakery, R)

    home_idx_list = [ i for i in range(building_n) if i not in mCoffee and i not in mBakery ]

    min_dist = float('inf')

    for home_idx in home_idx_list:
        if cafe_min_dist_list[home_idx] > R or bake_min_dist_list[home_idx] > R:
            continue
        total_dist = cafe_min_dist_list[home_idx] + bake_min_dist_list[home_idx]
        min_dist = min(min_dist, total_dist)

    if min_dist == float('inf'):
        return -1
    else:
        return min_dist