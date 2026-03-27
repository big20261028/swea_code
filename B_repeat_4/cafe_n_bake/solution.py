from collections import defaultdict
from heapq import heappop, heappush, heapify


city_n = 0
building_roads = defaultdict(list)


def multi_dijkstra(target_list, R):
    min_dist_list = [float('inf')] * city_n

    hq = []
    for _id in target_list:
        min_dist_list[_id] = 0
        hq.append((0, _id))
    heapify(hq)

    while hq:
        distance, node = heappop(hq)
        if distance > min_dist_list[node]:
            continue
        if distance > R:
            continue

        for next_node, next_dist in building_roads[node]:
            total_dist = distance + next_dist
            # if total_dist < min_dist_list[next_node]:
            #     min_dist_list[next_node] = total_dist
            #     if total_dist <= R:
            #         heappush(hq, (total_dist, next_node))
            if total_dist < min_dist_list[next_node] and total_dist <= R:
                min_dist_list[next_node] = total_dist
                heappush(hq, (total_dist, next_node))

    return min_dist_list


def init(N, K, sBuilding, eBuilding, mDistance):
    global city_n, building_roads
    city_n = N
    building_roads = defaultdict(list)

    for i in range(K):
        building_roads[sBuilding[i]].append((eBuilding[i], mDistance[i]))
        building_roads[eBuilding[i]].append((sBuilding[i], mDistance[i]))


def add(sBuilding, eBuilding, mDistance):
    building_roads[sBuilding].append((eBuilding, mDistance))
    building_roads[eBuilding].append((sBuilding, mDistance))


def calculate(M, mCoffee, P, mBakery, R):
    cafe_min_distances = multi_dijkstra(mCoffee, R)
    bake_min_distances = multi_dijkstra(mBakery, R)

    result = float('inf')

    #home_idx = [ idx for idx in range(city_n) if idx not in mCoffee and idx not in mBakery ]
    none_home_idx = set(mCoffee + mBakery)
    home_idx = [ idx for idx in range(city_n) if idx not in none_home_idx ]

    for node in home_idx:
        # if node in none_home_idx:
        #     continue
        if cafe_min_distances[node] > R or bake_min_distances[node] > R:
            continue
        total_dist = cafe_min_distances[node] + bake_min_distances[node]
        result = min(result, total_dist)

    if result == float('inf'):
        return -1
    else:
        return result