from typing import List

from heapq import heappush, heappop

class Result:
    def __init__(self, mX, mY, mMoveDistance, mRideDistance):
        self.mX = mX
        self.mY = mY
        self.mMoveDistance = mMoveDistance
        self.mRideDistance = mRideDistance


city_n = 0
call_limit = 0
taxi_info = {} # taxi_info[taxi_num] = [ (x, y), total_move, custom_move ]
bucket_n = 0
buckets = [[]]
mvp_taxi_heap = []


def init(N : int, M : int, L : int, mXs : List[int], mYs : List[int]) -> None:
    global city_n, call_limit, taxi_info, bucket_n, buckets, mvp_taxi_heap
    city_n = N
    call_limit = L
    taxi_info = {}
    bucket_n = N // L
    buckets = [ [set() for _ in range(bucket_n + 1)] for _ in range(bucket_n + 1) ]
    mvp_taxi_heap = []

    for i in range(M):
        taxi_info[i+1] = [(mXs[i], mYs[i]), 0, 0]
        bx, by = mXs[i] // call_limit, mYs[i] // call_limit
        buckets[bx][by].add(i+1)
        heappush(mvp_taxi_heap, (0, i+1))


def pickup(mSX : int, mSY : int, mEX : int, mEY : int) -> int:
    bx, by = mSX // call_limit, mSY // call_limit

    target_distance = float('inf')
    target_num = float('inf')

    for dx in range(-1, 2):
        for dy in range(-1, 2):
            bnx, bny = bx + dx, by + dy
            if not (0 <= bnx < bucket_n + 1 and 0 <= bny < bucket_n + 1):
                continue

            for taxi_num in buckets[bnx][bny]:
                (t_x, t_y), total_move, custom_move = taxi_info[taxi_num]
                distance = abs(t_x - mSX) + abs(t_y - mSY)
                if distance > call_limit: continue

                if distance < target_distance:
                    target_distance = distance
                    target_num = taxi_num
                elif distance == target_distance and taxi_num < target_num:
                    target_num = taxi_num

    if target_num == float('inf'):
        return -1

    dist_taxi_start = target_distance
    dist_start_end = abs(mSX - mEX) + abs(mSY - mEY)

    total_distance = dist_taxi_start + dist_start_end
    customer_move_distance = dist_start_end

    (t_x, t_y), old_total, old_custom = taxi_info[target_num]

    new_total = old_total + total_distance
    new_custom = old_custom + customer_move_distance

    taxi_info[target_num] = [ (mEX, mEY), new_total, new_custom ]

    box, boy = t_x // call_limit, t_y // call_limit
    buckets[box][boy].remove(target_num)

    bex, bey = mEX // call_limit, mEY // call_limit
    buckets[bex][bey].add(target_num)

    heappush(mvp_taxi_heap, (-new_custom, target_num))

    return target_num

def reset(mNo : int) -> Result:
    (t_x, t_y), total_dist, custom_dist = taxi_info[mNo]
    taxi_info[mNo] = [(t_x, t_y), 0, 0]
    heappush(mvp_taxi_heap, (0, mNo))

    return Result(t_x, t_y, total_dist, custom_dist)

def getBest(mNos : List[int]) -> None:
    need_taxi_count = len(mNos)

    cnt = 0
    repair = []
    target_list = []
    while mvp_taxi_heap and cnt < need_taxi_count:
        custom_dist, taxi_num = heappop(mvp_taxi_heap)
        custom_dist = -custom_dist

        (r_x, r_y), real_total, real_custom = taxi_info[taxi_num]
        if custom_dist != real_custom:
            continue
        # if taxi_num in mNos:
        #     continue
        if taxi_num in target_list:
            continue

        #mNos[cnt] = taxi_num
        target_list.append(taxi_num)
        cnt += 1

        repair.append((-custom_dist, taxi_num))

    for dist, num in repair:
        heappush(mvp_taxi_heap, (dist, num))

    for idx, num in enumerate(target_list):
        mNos[idx] = num