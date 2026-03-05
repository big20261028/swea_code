from typing import List
from collections import defaultdict

# 지점의 개수
n = 0
# 도로의 정보 | 도로ID : 지점1, 지점2, 길이
load_dict = {}
# 지점 별 도로 정보 | 지점 Index : [ 도로ID, .....]
point_dict = defaultdict(set)

# tc 처음에 호출 (초기화)
def init(N: int) -> None:
    global n, load_dict, point_dict
    n = N
    load_dict.clear()
    point_dict = defaultdict(set)

# K 개의 mSpotA[]지점과 mSpotB[]지점을 연결하는 아이디가 mID[], 길이가 mLen[]인 도로들이 추가
# mSpotA[i]지점과 mSpotB[i]지점은 서로 다른 지점이고, 연결하는 도로가 없음이 보장된다. ( 0 ≤ i ≤ K-1 )
# 추가되는 도로들의 아이디 mID[] 는 모두 서로 다르고, 기존 추가된 도로의 아이디와 서로 다르다.
def addRoad(K: int, mID: List[int], mSpotA: List[int], mSpotB: List[int], mLen: List[int]) -> None:
    for i in range(K):
        load_dict[mID[i]] = [mSpotA[i], mSpotB[i], mLen[i]]
        point_dict[mSpotA[i]].add(mID[i])
        point_dict[mSpotB[i]].add(mID[i])

# mID 도로를 삭제한다.
# mID 도로가 없거나 mID 도로가 이미 삭제되었을 수도 있다.
def removeRoad(mID: int) -> None:
    if mID not in load_dict:
        return

    point_a, point_b, _ = load_dict[mID]

    del load_dict[mID]
    point_dict[point_a].remove(mID)
    point_dict[point_b].remove(mID)


#  42195 이하의 길이가 가장 긴 마라톤 코스의 길이 반환
def getLength(mSpot: int) -> int:
    maraton_dist = 42195
    # 출발지점으로부터 4번 이동한 지점 정보 저장
    # 지점 번호, 사용한 길 ID 리스트, 거리
    move_data_dict = defaultdict(list)

    def dfs(point,length, path):
        if len(path) == 4:
            move_data_dict[point].append((length, set(path)))
            return

        for road_id in point_dict[point]:
            point_a, point_b, dist = load_dict[road_id]
            next_point = point_a if point != point_a else point_b
            #next_point = point_a + point_b - point
            if road_id in path or next_point == mSpot:
                continue
            path.add(road_id)
            dfs(next_point, length + dist, path)
            path.remove(road_id)

    dfs(mSpot, 0, set())

    result = -1

    for point in move_data_dict:
        for len_a, path_a in move_data_dict[point]:
            for len_b, path_b in move_data_dict[point]:
                # 도착지점에서 출발지점으로 가는 경로 탐색
                total_len = len_a + len_b
                if total_len > maraton_dist:
                    continue
                for road_id in path_a:
                    if road_id in path_b:
                        break
                else:
                    result = max(result, total_len)

    return result