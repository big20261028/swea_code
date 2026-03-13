from heapq import heappop,heappush
from collections import defaultdict

build_n = 0
building_roads = defaultdict(list) # 건물주소 : [ (거리, 목표건물주소), (거리, 목표건물주소), ... ]

# 시작지점 st_n 부터 각 지점까지의 최단거리 리턴
def dijkstra(st_n):
	fast_paths = [float('inf')] * build_n
	# fast_paths[st_n] = 0
	hq = [(0, st_n)]
	while hq:
		dist, pos = heappop(hq)
		if dist > fast_paths[pos]:
			continue
		for next_dist, next_pos in building_roads[pos]:
			total_dist = dist + next_dist
			if next_pos == st_n: continue
			if total_dist < fast_paths[next_pos]:
				fast_paths[next_pos] = total_dist
				heappush(hq, (total_dist, next_pos))
	return fast_paths


def init(N, K, sBuilding, eBuilding, mDistance):
	global build_n, building_roads

	build_n = N
	building_roads = defaultdict(list)

	for i in range(K):
		building_roads[sBuilding[i]].append((mDistance[i], eBuilding[i]))
		building_roads[eBuilding[i]].append((mDistance[i], sBuilding[i]))


def add(sBuilding, eBuilding, mDistance):
	building_roads[sBuilding].append((mDistance, eBuilding))
	building_roads[eBuilding].append((mDistance, sBuilding))


def calculate(M, mCoffee, P, mBakery, R):
	coffee_set = set(mCoffee)
	bakery_set = set(mBakery)

	cafe_dists = [dijkstra(cafe) for cafe in mCoffee]
	bakery_dists = [dijkstra(bakery) for bakery in mBakery]

	min_dist_total = float('inf')

	for i in range(build_n):
		if i in coffee_set or i in bakery_set:
			continue
		min_cafe = float('inf')
		min_bake = float('inf')

		for c_dist_list in cafe_dists:
			if c_dist_list[i] <= R:
				min_cafe = min(min_cafe, c_dist_list[i])

		for b_dist_list in bakery_dists:
			if b_dist_list[i] <= R:
				min_bake = min(min_bake, b_dist_list[i])

		if min_cafe == float('inf') or min_bake == float('inf'):
			continue

		dist_total = min_cafe + min_bake
		min_dist_total = min(min_dist_total, dist_total)

	if min_dist_total == float('inf'):
		return -1
	else:
		return min_dist_total