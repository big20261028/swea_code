from typing import List
from collections import defaultdict
from heapq import heappush,heappop

# 도시 한변의 길이
city_n = 0
# 연결제한
limit = 0
# 통신기 id별 정보
device_info = {} # 통신기ID : [ (my, mx), 고유주파수 ]
# 통신기 id별 최소 파워 연결지
best_device_to_device = defaultdict(list) # 통신기ID: [ (필요파워, 통신기ID), .... ] - 힙으로 관리


def init(N : int, mLimit : int) -> None:
    global city_n, limit, device_info, best_device_to_device
    city_n = N
    limit = mLimit
    device_info.clear()
    best_device_to_device = defaultdict(list)


def addRadio(K : int, mID : List[int], mFreq : List[int], mY : List[int], mX : List[int]) -> None:

    for i in range(K):
        dv_id, freq, dv_y, dv_x = mID[i], mFreq[i], mY[i], mX[i]
        device_info[dv_id] = [(dv_y, dv_x), freq]

        # 새로 추가된 장비와 기존에 있던 장비간 연결 비용 추가
        for other_id, item in device_info.items():
            if other_id == dv_id: continue
            (oy, ox), o_freq = item

            dist = abs(dv_y - oy) + abs(dv_x - ox)
            need_power = dist * 10
            if o_freq != freq:
                need_power += 1000

            heappush(best_device_to_device[dv_id], (need_power, other_id))
            heappush(best_device_to_device[other_id], (need_power, dv_id))


def getMinPower(mID : int, mCount : int) -> int:
    return 0