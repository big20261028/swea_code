from typing import List

from collections import defaultdict

n = 0
spot_loads = defaultdict(set)
loads = defaultdict(int)

cos_len = 42195

def init(N: int) -> None:
    global n, spot_loads, loads
    n = N
    spot_loads = defaultdict(set)
    loads = {}


def addRoad(K: int, mID: List[int], mSpotA: List[int], mSpotB: List[int], mLen: List[int]) -> None:

    for i in range(K):
        spot_loads[mSpotA[i]].add(mID[i])
        spot_loads[mSpotB[i]].add(mID[i])
        loads[mID[i]] = [mLen[i], mSpotA[i], mSpotB[i]]


def removeRoad(mID: int) -> None:
    if mID not in loads: return

    l, s1, s2 = loads[mID]
    spot_loads[s1].remove(mID)
    spot_loads[s2].remove(mID)
    del loads[mID]


def getLength(mSpot: int) -> int:
    courses = defaultdict(list)

    def dfs(p, length, visited):
        if len(visited) == 4:
            courses[p].append((length, set(visited)))
            return
        # p에 이어진 모든 경로 탐색
        # 도로 아이디는 1부터 시작
        # 지점 번호도 1부터 시작
        for load_id in spot_loads[p]:
            load_len, pos_a, pos_b = loads[load_id]
            end_p = (pos_a + pos_b) - p
            # mSpot 지점은 출발지점과 도착지점을 제외하고 지나가지 않음
            if end_p == mSpot:
                continue
            # 이미 지나온 경로라면 continue
            elif load_id in visited:
                continue
            visited.add(load_id)
            dfs(end_p,length + load_len, visited)
            visited.remove(load_id)

    dfs(mSpot, 0, set())

    result = -1

    # course의 값은 중간 경유지점 : [ set(경로 아이디들), set(경로 아이디들)....]
    for key in courses:
        for len_a, cos_a in courses[key]:
            for len_b, cos_b in courses[key]:
                total_dist = len_a + len_b

                if total_dist > cos_len:
                    continue

                for load_id in cos_a:
                    if load_id in cos_b:
                        break
                else:
                    result = max(result, total_dist)

    return result