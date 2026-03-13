from heapq import heappop, heappush

empty_hq = []
building_info = {}
start_pos = {}
end_pos = {}

# left_idx ~ right_idx 사이의 빈공간 데이터 제거
def remove_pos(left_idx, right_idx):
    start_pos.pop(left_idx, None)
    end_pos.pop(right_idx, None)

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

        remove_pos(left_idx, right_idx)

        remain_cnt = length - mLength
        building_start = left_idx + (remain_cnt // 2)
        building_end_next = building_start + mLength

        building_info[building_start] = mLength
        # 수정
        add_pos(left_idx, building_start -1)
        add_pos(building_end_next, right_idx)

        return building_start

    return -1


def demolish(mAddr: int) -> int:
    building_length = building_info.pop(mAddr,None)
    if building_length is None:
        return -1

    b_st, b_end = mAddr, mAddr + building_length - 1

    left_empty_pos = end_pos.get(b_st - 1)
    right_empty_pos = start_pos.get(b_end + 1)

    if left_empty_pos is not None:
        remove_pos(left_empty_pos, b_st -1)
        b_st = left_empty_pos
    if right_empty_pos is not None:
        remove_pos(b_end+1, right_empty_pos)
        b_end = right_empty_pos

    add_pos(b_st, b_end)

    return building_length
