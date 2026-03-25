from collections import defaultdict
from heapq import heappop,heappush

city_n = 0
city_loads = defaultdict(list)


def dijkstra(st_node):
	max_weights = [float('-inf')] * city_n
	max_weights[st_node] = float('-inf')
	hq = [(float('-inf'), st_node)]
	while hq:
		weight, node = heappop(hq)
		weight = -weight
		if weight < max_weights[node] and weight != float('inf'):
			continue
		for next_weight, next_node in city_loads[node]:
			need_weight = min(weight, next_weight)
			if need_weight > max_weights[next_node]:
				max_weights[next_node] = need_weight
				heappush(hq, (-need_weight, next_node))

	return max_weights


def init(N, K, sCity, eCity, mLimit):
	global city_n, city_loads
	city_n = N
	city_loads = defaultdict(list)

	for i in range(K):
		city_loads[sCity[i]].append((mLimit[i], eCity[i]))
		city_loads[eCity[i]].append((mLimit[i], sCity[i]))


def add(sCity, eCity, mLimit):
	city_loads[sCity].append((mLimit, eCity))
	city_loads[eCity].append((mLimit, sCity))


def calculate(sCity, eCity, M, mStopover):
	targets = [sCity] + mStopover + [eCity]
	max_weights_targets = {}
	for target in targets:
		max_weights_targets[target] = dijkstra(target)
	# print(max_weights_targets)

	min_weight = float('inf')
	for i in range(M+1):
		need_w = max_weights_targets[targets[i]][targets[i+1]]
		if need_w == float('-inf'):
			min_weight = float('inf')
			break
		min_weight = min(min_weight, need_w)

	# print(min_weight)

	if min_weight == float('inf'):
		return -1
	else:
		return min_weight