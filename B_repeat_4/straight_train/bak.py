from collections import defaultdict
from math import lcm
from heapq import heappop, heappush

# station_n = 0
connected_trains = defaultdict(set) # [기차 ID] = [연결된 기차 ID, 연결된 기차 ID, ... ]
train_info = {} # 기차 ID = [시작역, 종착역, 간격]


def is_stop(station, train_data):
    start, end, term = train_data['start'], train_data['end'], train_data['term']
    if not (start <= station <= end):
        return False

    if (station - start) % term == 0:
        return True
    return False


def is_connected(t1, t2):
    # 두 기차의 운송 경로가 겹치는지 확인
    st_station = max(t1['start'], t2['start'])
    end_station = min(t1['end'], t2['end'])

    if st_station > end_station:
        return False

    max_range = lcm(t1['term'], t2['term'])
    limit = min(end_station, st_station + max_range)

    for station in range(st_station, limit + 1):
        t1_is_stop = (station - t1['start']) % t1['term'] == 0
        t2_is_stop = (station - t2['start']) % t2['term'] == 0

        if t1_is_stop and t2_is_stop:
            return True

    return False


def init(N, K, mId, sId, eId, mInterval):
    global connected_trains, train_info
    connected_trains = defaultdict(set)
    train_info = {}
    for i in range(K):
        add(mId[i], sId[i], eId[i], mInterval[i])


def add(mId, sId, eId, mInterval):
    new_train = {'start':sId, 'end':eId, 'term':mInterval}
    for train_id, train_data in train_info.items():
        # 두 열차가 연결되어 있는지 확인 (환승가능한지)
        if is_connected(new_train, train_data):
            connected_trains[mId].add(train_id)
            connected_trains[train_id].add(mId)

    train_info[mId] = new_train


def remove(mId):
    for train in connected_trains[mId]:
        connected_trains[train].remove(mId)

    del connected_trains[mId]
    del train_info[mId]


def multi_dijkstra(target_list, end_list):
    min_distance_list = { train_id : float('inf') for train_id in train_info }
    hq = []
    for target_id in target_list:
        min_distance_list[target_id] = 0
        heappush(hq, (0, target_id))

    while hq:
        dist, pos = heappop(hq)
        if dist > min_distance_list[pos]:
            continue
        if pos in end_list:
            return dist

        for next_train_id in connected_trains[pos]:
            next_dist = dist + 1
            if next_dist < min_distance_list[next_train_id]:
                min_distance_list[next_train_id] = next_dist
                heappush(hq, (next_dist, next_train_id))
    return -1

def calculate(sId, eId):
    start_train = set()
    end_train = set()
    for train_id, train_data in train_info.items():
        is_start_pos = is_stop(sId, train_data)
        is_end_pos = is_stop(eId, train_data)
        if is_start_pos and is_end_pos:
            return 0
        if is_start_pos:
            start_train.add(train_id)
        elif is_end_pos:
            end_train.add(train_id)
    if not start_train or not end_train:
        return -1

    return multi_dijkstra(start_train, end_train)