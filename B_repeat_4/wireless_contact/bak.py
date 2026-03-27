from typing import List

from heapq import heappop, heappush, heapify

city_n = 0
power_limit = 0
limit_distance = 0

device_info = {} # device_info[dv_id] = [ (mY, mX), Fg ]
buckets = [[]]

def init(N : int, mLimit : int) -> None:
    global city_n, power_limit, device_info, buckets, limit_distance
    city_n = N
    power_limit = mLimit
    limit_distance = mLimit // 10

    device_info = {}
    buckets = [ [set() for _ in range(city_n // limit_distance + 1)] for _ in range(city_n // limit_distance + 1) ]


def addRadio(K : int, mID : List[int], mFreq : List[int], mY : List[int], mX : List[int]) -> None:
    for i in range(K):
        device_info[mID[i]] = [(mY[i], mX[i]), mFreq[i]]
        by, bx = mY[i] // limit_distance, mX[i] // limit_distance
        buckets[by][bx].add(mID[i])


def getMinPower(mID : int, mCount : int) -> int:
    (t_y, t_x), t_fg = device_info[mID]
    by, bx = t_y // limit_distance, t_x // limit_distance

    bucket_n = len(buckets)

    min_power_device = []

    for dy in range(-1, 2):
        for dx in range(-1, 2):
            bny, bnx = by + dy, bx + dx
            if not (0 <= bny < bucket_n and 0 <= bnx < bucket_n):
                continue

            for dv_id in buckets[bny][bnx]:
                if dv_id == mID: continue

                (dv_y, dv_x), dv_fg = device_info[dv_id]
                dist = abs(dv_y - t_y) + abs(dv_x - t_x)
                cost = dist * 10
                if dv_fg != t_fg:
                    cost += 1000

                if cost > power_limit:
                    continue

                min_power_device.append((cost, dv_id))

    heapify(min_power_device)
    min_power = 0
    cnt = 0
    while min_power_device and cnt < mCount:
        cost, _ = heappop(min_power_device)
        min_power += cost
        cnt += 1


    return min_power