from typing import List
from collections import defaultdict

city_n = 0
city_roads = defaultdict(set) # 도시번호 : [ (도착번호, 도로번호) ....]
road_info = {} # 도로번호 : (길이, 지점1, 지점2)


def init(N: int) -> None:
    global city_n, city_roads, road_info
    city_n = N
    city_roads = defaultdict(set)
    road_info.clear()


def addRoad(K: int, mID: List[int], mSpotA: List[int], mSpotB: List[int], mLen: List[int]) -> None:
    for i in range(K):
        city_roads[mSpotA[i]].add((mSpotB[i], mID[i]))
        city_roads[mSpotB[i]].add((mSpotA[i], mID[i]))
        road_info[mID[i]] = (mLen[i], mSpotA[i], mSpotB[i])

    # print(city_roads)
    # print(road_info)


def removeRoad(mID: int) -> None:
    if mID not in road_info:
        return mID

    length, pos1, pos2 = road_info.pop(mID)
    city_roads[pos1].remove((pos2, mID))
    city_roads[pos2].remove((pos1, mID))


def getLength(mSpot: int) -> int:
    maraton_cos = 42195
    roads_dict = defaultdict(list) # 도착좌표: [(사용도로 아이디 4개), (사용도로 아이디 4개) ... ]

    def find_path(node, length, visited):
        if len(visited) == 4:
            roads_dict[node].append((length, set(visited)))
            return

        for next_node, road_id in city_roads[node]:
            if next_node == mSpot:
                continue
            if road_id in visited:
                continue
            road_len = road_info[road_id][0]
            find_path(next_node,length + road_len, visited + [road_id])

    find_path(mSpot, 0, [])

    # print(roads_dict)
    max_path_len = -1
    for key in roads_dict:
        for len_a, roads_a in roads_dict[key]:
            for len_b, roads_b in roads_dict[key]:
                total_len = len_a + len_b
                if total_len > maraton_cos:
                    continue
                for road_id in roads_a:
                    if road_id in roads_b:
                        break
                else:
                    max_path_len = max(max_path_len, total_len)
    return max_path_len