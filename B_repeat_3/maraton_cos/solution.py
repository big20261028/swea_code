from typing import List

from collections import defaultdict

'''
실수한점

경로 탐색 후 dfs 종료를 위한 return 누락
'''

FULL_DISTANCE = 42195

city_n = 0
city_roads = defaultdict(set)
road_info = {}


def init(N: int) -> None:
    global city_n, road_info, city_roads
    city_n = N
    city_roads = defaultdict(set)
    road_info = {}


def addRoad(K: int, mID: List[int], mSpotA: List[int], mSpotB: List[int], mLen: List[int]) -> None:

    for i in range(K):
        road_info[mID[i]] = (mSpotA[i], mSpotB[i], mLen[i])
        city_roads[mSpotA[i]].add((mID[i], mSpotB[i], mLen[i]))
        city_roads[mSpotB[i]].add((mID[i], mSpotA[i], mLen[i]))


def removeRoad(mID: int) -> None:
    if mID not in road_info:
        return
    a_pos, b_pos, road_len = road_info.pop(mID)
    city_roads[a_pos].remove((mID, b_pos, road_len))
    city_roads[b_pos].remove((mID, a_pos, road_len))


'''
mSpot으로부터 각 지점까지의 경로 계산
각 지점을 마지막 노드로 하는 길, 4개의 길 

'''
def getLength(mSpot: int) -> int:
    # 경유 노드 = [(도로번호 4개),(도로번호 4개),(도로번호 4개), ....]
    candidate_paths = defaultdict(list)

    def find_path(node, total_len, visited):
        if len(visited) == 4:
            candidate_paths[node].append((total_len, set(visited)))
            return

        for road_id, next_node, dist in city_roads[node]:
            if next_node == mSpot: continue

            if road_id in visited: continue

            find_path(next_node, total_len+dist, visited + [road_id])

    find_path(mSpot, 0, [])

    # 가장 길이가 긴 마라톤 코스 길이 반환
    max_cos_dist = -1

    for key in candidate_paths:
        for a_dist, a_roads in candidate_paths[key]:
            for b_dist, b_roads in candidate_paths[key]:
                total_dist = a_dist + b_dist
                if total_dist > FULL_DISTANCE: continue
                for road_id in a_roads:
                    if road_id in b_roads: break
                else:
                    max_cos_dist = max(max_cos_dist, total_dist)

    return max_cos_dist