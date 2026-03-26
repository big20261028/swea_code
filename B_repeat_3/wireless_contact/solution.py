from typing import List
from heapq import heappop, heappush
'''
거리 1당 필요 파워 10
주파수가 다를 경우 필요한 파워 1000 추가
파워 제한이 2000일 경우 200칸이 최대
한 지점에서 주변 다른 지점까지 최대로 갈 수 있는 범위가 200칸이므로 버킷의 크기는 200칸이 필요함

'''

city_n = 0
power_limit = 0
device_info = {} # [통신기 ID] = [고유주파수, 좌표]
buckets = [[]]
bucket_size = 0

def init(N : int, mLimit : int) -> None:
    global city_n, power_limit, device_info, buckets, bucket_size
    city_n = N
    power_limit = mLimit
    device_info = {}
    bucket_size = (power_limit // 10)
    buckets = [ [set() for _ in range(N // bucket_size + 1)] for _ in range(N // bucket_size + 1) ]


def addRadio(K : int, mID : List[int], mFreq : List[int], mY : List[int], mX : List[int]) -> None:

    for i in range(K):
        device_info[mID[i]] = [mFreq[i], (mY[i], mX[i])]
        by, bx = mY[i] // bucket_size, mX[i] // bucket_size
        buckets[by][bx].add(mID[i])


def getMinPower(mID : int, mCount : int) -> int:
    target_freq, (t_y, t_x) = device_info[mID]
    by, bx = t_y // bucket_size, t_x // bucket_size
    bucket_n = len(buckets)

    min_power_hp = []

    for bdy in range(-1, 2):
        for bdx in range(-1,2):
            bny, bnx = by + bdy, bx + bdx
            if not (0 <= bny < bucket_n and 0 <= bnx < bucket_n):
                continue

            for device_id in buckets[bny][bnx]:
                if device_id == mID: continue

                freq, (y, x) = device_info[device_id]

                dist = abs(t_y - y) + abs(t_x - x)
                need_cost = (dist * 10)
                if freq != target_freq:
                    need_cost += 1000

                if need_cost > power_limit:
                    continue

                heappush(min_power_hp, (need_cost, device_id))
    #print(min_power_hp)
    total_power = 0
    cnt = 0
    while min_power_hp and cnt < mCount:
        cost, dv_id = heappop(min_power_hp)
        total_power += cost
        cnt += 1

    return total_power