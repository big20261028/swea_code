from heapq import heappush, heappop


empty_hq = [] # [ (길이, 시작좌표), (길이, 시작좌표), ..... ]
building_info = {} # 빌딩 인덱스 : 길이
start_pos = {} # 빈공간 시작 인덱스 : 끝 인덱스
end_pos = {} # 빈공간 끝 인덱스 : 시작 인덱스

def remove_pos(left_idx, right_idx):
    end_pos.pop(right_idx)
    start_pos.pop(left_idx)

def add_pos(left_idx, right_idx):
    if left_idx > right_idx:
        return
    start_pos[left_idx] = right_idx
    end_pos[right_idx] = left_idx
    length = right_idx - left_idx + 1
    heappush(empty_hq, (-length, left_idx))


def init(N: int) -> None:
    global empty_hq, building_info, start_pos, end_pos
    empty_hq = []
    building_info = {}
    start_pos = {}
    end_pos = {}
    add_pos(0, N-1)


def build(mLength: int) -> int:
    while empty_hq:
        length, left_idx = heappop(empty_hq)
        length = -length
        right_idx = start_pos.get(left_idx)
        if right_idx is None:
            continue
        real_len = right_idx - left_idx + 1
        if real_len != length:
            continue

        if length < mLength:
            heappush(empty_hq, (-length, left_idx))
            return -1

        remove_pos(left_idx,right_idx)

        remain_cnt = length - mLength
        building_start = left_idx + (remain_cnt//2)
        building_end_next = building_start + mLength

        building_info[building_start] = mLength
        add_pos(left_idx, building_start-1)
        add_pos(building_end_next, right_idx)
        return building_start

    return -1


def demolish(mAddr: int) -> int:
    building_len = building_info.pop(mAddr, None)
    if building_len is None:
        return -1

    building_st = mAddr
    building_end = mAddr + building_len - 1

    left_empty_idx = end_pos.get(building_st - 1)
    right_empty_idx = start_pos.get(building_end + 1)

    if left_empty_idx is not None:
        remove_pos(left_empty_idx, building_st-1)
        building_st = left_empty_idx

    if right_empty_idx is not None:
        remove_pos(building_end + 1, right_empty_idx)
        building_end = right_empty_idx

    add_pos(building_st, building_end)

    return building_len
