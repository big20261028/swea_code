
from heapq import heappop, heappush

city_n = 0 # 도시 길이
empty_areas = [] # 빈 구역 시작 인덱스
# 빈 구역의 크기를 저장하기 위한 딕셔너리 2개
start_pos = {} # 시작 인덱스 = 끝 인덱스
end_pos = {} # 끝 인덱스 = 시작 인덱스
building_info = {} # 빌딩 주소 = 길이


def delete_pos(left_pos, right_pos):
    start_pos.pop(left_pos)
    end_pos.pop(right_pos)


def add_pos(left_pos, right_pos):
    if left_pos > right_pos:
        return
    start_pos[left_pos] = right_pos
    end_pos[right_pos] = left_pos
    length = right_pos - left_pos + 1
    heappush(empty_areas, (-length, left_pos))


def init(N: int) -> None:
    global city_n, empty_areas, start_pos, end_pos, building_info
    city_n = N
    empty_areas = []
    start_pos = {}
    end_pos = {}
    building_info = {}
    add_pos(0, N-1)


def build(mLength: int) -> int:
    while empty_areas:
        length, left_pos = heappop(empty_areas)
        length = -length
        right_pos = start_pos.get(left_pos)
        if right_pos is None:
            continue
        real_length = right_pos - left_pos + 1
        if real_length != length:
            continue

        if length < mLength:
            heappush(empty_areas, (-length, left_pos))
            return -1

        delete_pos(left_pos, right_pos)

        remain_area_cnt = length - mLength
        building_start_idx = left_pos + (remain_area_cnt // 2)
        building_end_next_idx = building_start_idx + mLength

        building_info[building_start_idx] = mLength
        add_pos(left_pos, building_start_idx - 1)
        add_pos(building_end_next_idx, right_pos)

        return building_start_idx

    return -1

def demolish(mAddr: int) -> int:
    building_length = building_info.pop(mAddr, None)
    if building_length is None:
        return -1

    building_start_idx = mAddr
    building_end_idx = mAddr + building_length - 1

    left_pos = end_pos.get(building_start_idx - 1)
    right_pos = start_pos.get(building_end_idx + 1)

    if left_pos is not None:
        delete_pos(left_pos, building_start_idx - 1)
        building_start_idx = left_pos
    if right_pos is not None:
        delete_pos(building_end_idx + 1, right_pos)
        building_end_idx = right_pos

    add_pos(building_start_idx, building_end_idx)

    return building_length
