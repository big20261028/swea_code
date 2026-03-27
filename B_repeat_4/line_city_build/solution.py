from collections import defaultdict
from heapq import heappop, heappush

city_n = 0
empty_hq = [] # [ (length, idx), (length, idx) ... ]
start_idx = {} # start_idx[left_idx] = right_idx
end_idx = {} # end_idx[right_idx] = left_idx
building_info = {} # building_info[left_idx] = length


def remove_idx(left_idx, right_idx):
    start_idx.pop(left_idx)
    end_idx.pop(right_idx)


def add_idx(left_idx, right_idx):
    if left_idx > right_idx:
        return
    start_idx[left_idx] = right_idx
    end_idx[right_idx] = left_idx
    length = right_idx - left_idx + 1
    heappush(empty_hq, (-length, left_idx))


def init(N: int) -> None:
    global city_n, empty_hq, start_idx, end_idx, building_info
    city_n = N
    empty_hq = []
    start_idx.clear()
    end_idx.clear()
    building_info.clear()

    add_idx(0, N-1)


def build(mLength: int) -> int:
    while empty_hq:
        length, left_idx = heappop(empty_hq)
        length = -length
        right_idx = start_idx.get(left_idx)
        if right_idx is None:
            continue
        real_len = right_idx - left_idx + 1
        if real_len != length:
            continue
        if length < mLength:
            heappush(empty_hq, (-length, left_idx))
            return -1

        remove_idx(left_idx, right_idx)

        remain_area = length - mLength
        building_start_idx = left_idx + (remain_area // 2)
        building_end_next_idx = building_start_idx + mLength

        add_idx(left_idx, building_start_idx - 1)
        add_idx(building_end_next_idx, right_idx)
        building_info[building_start_idx] = mLength
        return building_start_idx

    return -1


def demolish(mAddr: int) -> int:
    building_len = building_info.pop(mAddr, None)
    if building_len is None:
        return -1

    building_start_idx = mAddr
    building_end_idx = mAddr + building_len - 1

    left_idx = end_idx.get(building_start_idx - 1)
    right_idx = start_idx.get(building_end_idx + 1)

    if left_idx is not None:
        remove_idx(left_idx, building_start_idx - 1)
        building_start_idx = left_idx
    if right_idx is not None:
        remove_idx(building_end_idx + 1, right_idx)
        building_end_idx = right_idx

    add_idx(building_start_idx, building_end_idx)
    length = building_start_idx - building_end_idx + 1
    heappush(empty_hq, (length, building_start_idx))

    return building_len
