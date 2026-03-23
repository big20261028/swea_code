from typing import List

from collections import defaultdict

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





    return 0