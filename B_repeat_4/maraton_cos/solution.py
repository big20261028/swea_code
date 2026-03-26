from typing import List

from collections import defaultdict

city_n = 0
road_info = {} # road_info[road_id] = [length, a_pos, b_pos]
node_roads = defaultdict(set)

MARATHON_DISTANCE = 42195

def init(N: int) -> None:
    global city_n, road_info, node_roads
    city_n = N
    road_info = {}
    node_roads = defaultdict(set)


def addRoad(K: int, mID: List[int], mSpotA: List[int], mSpotB: List[int], mLen: List[int]) -> None:

    for i in range(K):
        road_info[mID[i]] = [mLen[i], mSpotA[i], mSpotB[i]]
        node_roads[mSpotA[i]].add(mID[i])
        node_roads[mSpotB[i]].add(mID[i])


def removeRoad(mID: int) -> None:
    if mID not in road_info:
        return

    length, a_pos, b_pos = road_info.pop(mID)
    node_roads[a_pos].remove(mID)
    node_roads[b_pos].remove(mID)


def getLength(mSpot: int) -> int:

    path_dict = defaultdict(list)

    def dfs(node, distance, visited):
        if len(visited) == 4:
            path_dict[node].append((distance, set(visited)))
            return

        for road_id in node_roads[node]:
            if road_id in visited: continue

            road_dist, a_node, b_node = road_info[road_id]
            next_node = (a_node + b_node) - node
            if next_node == mSpot: continue

            need_dist = distance + road_dist
            if need_dist > MARATHON_DISTANCE:
                continue

            dfs(next_node, need_dist, visited + [road_id])

    dfs(mSpot, 0, [])

    max_distance = -1

    for key in path_dict:
        for a_dist, a_roads in path_dict[key]:
            for b_dist, b_roads in path_dict[key]:
                total_dist = a_dist + b_dist
                if total_dist > MARATHON_DISTANCE: continue

                for road_id in a_roads:
                    if road_id in b_roads:
                        break
                else:
                    max_distance = max(max_distance, total_dist)

    return max_distance