from math import gcd
from collections import defaultdict
from heapq import heappop, heappush

trains = {}
connect_trains = defaultdict(set)


def is_visit(station, train_info):
    start, end, term = train_info['start'], train_info['end'], train_info['term']
    if not (start <= station <= end):
        return False

    if (station - start) % term == 0:
        return True
    return False


def is_connected(t1, t2):
    st_station = max(t1['start'], t2['start'])
    end_station = min(t1['end'], t2['end'])

    if st_station > end_station:
        return False

    # lcm_val = lcm(t1['term'], t2['term'])
    gcd_val = gcd(t1['term'], t2['term'])
    # lcm_val = gcd_val * (t1['term'] // gcd_val) * (t2['term'] // gcd_val)
    lcm_val = (t1['term'] * t2['term']) // gcd_val
    limits = min(end_station, st_station + lcm_val)

    for station in range(st_station, limits + 1):
        t1_is_station = (station - t1['start']) % t1['term'] == 0
        t2_is_station = (station - t2['start']) % t2['term'] == 0
        if t1_is_station and t2_is_station:
            return True

    return False


def init(N, K, mId, sId, eId, mInterval):
    global trains, connect_trains
    trains = {}
    connect_trains = defaultdict(set)
    for i in range(K):
        add(mId[i], sId[i], eId[i], mInterval[i])


def add(mId, sId, eId, mInterval):
    new_train = { 'start' : sId, 'end' : eId, 'term' : mInterval }
    for train_id, train_info in trains.items():
        if is_connected(new_train, train_info):
            connect_trains[mId].add(train_id)
            connect_trains[train_id].add(mId)

    trains[mId] = new_train


def remove(mId):
    for train_id in connect_trains[mId]:
        connect_trains[train_id].remove(mId)

    del trains[mId]
    del connect_trains[mId]


def multi_dijkstra(target_list, end_list):
    min_distances = { train : float('inf') for train in trains }
    hq = []
    for target_id in target_list:
        min_distances[target_id] = 0
        heappush(hq, (0, target_id))

    while hq:
        dist, station = heappop(hq)
        if dist > min_distances[station]:
            continue

        if station in end_list:
            return dist

        for next_station in connect_trains[station]:
            next_dist = dist + 1
            if next_dist < min_distances[next_station]:
                min_distances[next_station] = next_dist
                heappush(hq, (next_dist, next_station))
    return -1

def calculate(sId, eId):
    start_station = set()
    end_station = set()
    for train_id, train_info in trains.items():
        is_start_pos = is_visit(sId, train_info)
        is_end_pos = is_visit(eId, train_info)
        if is_start_pos and is_end_pos:
            return 0
        if is_start_pos:
            start_station.add(train_id)
        if is_end_pos:
            end_station.add(train_id)

    if not start_station or not end_station:
        return -1

    return multi_dijkstra(start_station, end_station)