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

# 버킷
buckets = [[]]
# 버킷 제한 범위
bucket_limit = 0


def init(N : int, mLimit : int) -> None:
    global city_n, limit, device_info, best_device_to_device, buckets, bucket_limit
    city_n = N
    limit = mLimit
    device_info.clear()
    #best_device_to_device = defaultdict(list)
    bucket_limit = mLimit // 10
    buckets = [ [set() for _ in range(city_n // bucket_limit + 1)] for _ in range(city_n // bucket_limit + 1) ]


def addRadio(K : int, mID : List[int], mFreq : List[int], mY : List[int], mX : List[int]) -> None:

    for i in range(K):
        dv_id, freq, dv_y, dv_x = mID[i], mFreq[i], mY[i], mX[i]
        device_info[dv_id] = [(dv_y, dv_x), freq]

        by, bx = dv_y // bucket_limit, dv_x // bucket_limit
        buckets[by][bx].add(dv_id)
    # print(buckets)
    # print(city_n, limit)


def getMinPower(mID : int, mCount : int) -> int:

    min_power_data = []

    (dv_y, dv_x), freq = device_info[mID]
    by, bx = dv_y // bucket_limit, dv_x // bucket_limit

    bucket_len = len(buckets)

    for bdy in range(-1,2):
        for bdx in range(-1,2):
            nby, nbx = by + bdy, bx + bdx
            if not (0 <= nby < bucket_len and 0 <= nbx < bucket_len):
                continue
            for other_id in buckets[nby][nbx]:
                if other_id == mID:
                    continue
                (oy, ox), o_freq = device_info[other_id]
                dist = abs(dv_y - oy) + abs(dv_x - ox)
                need_power = dist * 10
                if o_freq != freq:
                    need_power += 1000

                if need_power > limit:
                    continue

                heappush(min_power_data, (need_power, other_id))

    cnt = 0
    min_power = 0
    while min_power_data and cnt < mCount:
        need_power, _ = heappop(min_power_data)
        min_power += need_power
        cnt += 1

    return min_power