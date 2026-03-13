from heapq import heappop,heappush

empty_hp = [] # [(길이, 인덱스), (길이, 인덱스) ....]
building_pos = {} # 빌딩 시작인덱스 : 길이
start_pos = {} # 빈공간 시작 인덱스: 끝 인덱스
end_pos = {} # 빈공간 끝 인덱스 : 시작 인덱스

def empty_remove(left_idx, right_idx):
    start_pos.pop(left_idx)
    end_pos.pop(right_idx)

def empty_add(left_idx, right_idx):
    if left_idx > right_idx:
        return
    start_pos[left_idx] = right_idx
    end_pos[right_idx] = left_idx
    length = (right_idx - left_idx) + 1
    heappush(empty_hp, (-length, left_idx))


def init(N: int) -> None:
    global empty_hp, building_pos, start_pos, end_pos
    empty_hp = []
    building_pos = {}
    start_pos = {}
    end_pos = {}
    empty_add(0, N-1)

def build(mLength: int) -> int:
    while empty_hp:
        length, st_i = heappop(empty_hp)
        length = -length
        # 진짜 빈 공간이 맞는지 확인
        end_i = start_pos.get(st_i)
        if end_i is None:
            continue
        # 빈 공간의 길이가 힙에 등록되어 있던 길이와 일치 하는지 확인(구식 정보처리)
        real_len = end_i - st_i + 1
        if length != real_len:
            continue
        # 빈 공간이 지어질 건물의 크기보다 작으면 함수 종료
        # 가장 큰 빈 공간부터 확인하므로 더 확인할 필요 없음
        if length < mLength:
            heappush(empty_hp, (-length, st_i))
            return -1

        # 기존의 빈공간 데이터 삭제
        empty_remove(st_i, end_i)

        # 빌딩의 좌표 선정
        remain_cnt = length - mLength
        building_st_i = st_i + (remain_cnt // 2) # 빌딩의 시작 좌표
        building_end_i = building_st_i + mLength # 빌딩 끝난 뒤 다음좌표

        # 정보 등록
        building_pos[building_st_i] = mLength
        empty_add(st_i, building_st_i-1)
        empty_add(building_end_i, end_i)
        return building_st_i
    return -1


def demolish(mAddr: int) -> int:
    target_len = building_pos.pop(mAddr,None)
    if target_len is None:
        return -1

    org_left_idx, org_right_idx = mAddr, mAddr + target_len - 1
    rest_left_idx = end_pos.get(org_left_idx - 1)
    rest_right_idx = start_pos.get(org_right_idx + 1)

    # 삭제할 빌딩 바로 왼쪽에 남은 구간 있으면 병합 대상
    if rest_left_idx is not None:
        empty_remove(rest_left_idx, org_left_idx - 1)
        org_left_idx = rest_left_idx

    # 삭제할 빌딩 바로 오른쪽에 남은 구간 있으면 병합 대상
    if rest_right_idx is not None:
        empty_remove(org_right_idx + 1, rest_right_idx)
        org_right_idx = rest_right_idx

    # 구간 병합
    empty_add(org_left_idx, org_right_idx)
    return target_len
