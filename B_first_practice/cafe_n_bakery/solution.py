from collections import defaultdict
from heapq import heappop, heappush

# 건물 개수
build_n = 0
# 건물 도로
building_roads = defaultdict(list) # 건물ID : [ (거리, 목표건물ID),(거리, 목표건물ID),(거리, 목표건물ID) ]


def dijkstra(target_list, R):
	min_dist_list = [float('inf')] * build_n
	hq = []
	for _id in target_list:
		min_dist_list[_id] = 0
		heappush(hq, (0, _id))

	while hq:
		dist, node = heappop(hq)
		if dist > R: break
		if dist > min_dist_list[node]: continue

		for next_dist, next_id in building_roads[node]:
			total_dist = dist + next_dist
			if total_dist < min_dist_list[next_id]:
				min_dist_list[next_id] = total_dist
				if total_dist <= R:
					heappush(hq, (total_dist, next_id))

	return min_dist_list


def init(N, K, sBuilding, eBuilding, mDistance):
	global build_n, building_roads
	build_n = N
	building_roads = defaultdict(list)

	for i in range(K):
		b_1, b_2, dist = sBuilding[i], eBuilding[i], mDistance[i]
		building_roads[b_1].append((dist, b_2))
		building_roads[b_2].append((dist, b_1))


def add(sBuilding, eBuilding, mDistance):
	building_roads[sBuilding].append((mDistance, eBuilding))
	building_roads[eBuilding].append((mDistance, sBuilding))


def calculate(M, mCoffee, P, mBakery, R):
	cafe_dist = dijkstra(mCoffee, R)
	bake_dist = dijkstra(mBakery, R)

	not_home_build_ids = set(mCoffee + mBakery)
	min_dist = float('inf')

	for i in range(build_n):
		if i in not_home_build_ids:
			continue
		if cafe_dist[i] <= R and bake_dist[i] <= R:
			min_dist = min(min_dist, cafe_dist[i] + bake_dist[i])

	if min_dist == float('inf'):
		return -1
	else:
		return min_dist