from typing import List
from collections import defaultdict

plane_n = 0
hash_info = {} # hash_info[좌표] = 해시값
hash_pos_data = defaultdict(list) # hash_pos_data[해시값] = [ 시작좌표, 시작좌표, .... ]
prefix_matrix = [[]]


def get_hash(st_x, st_y, matrix):
    hashes = []

    for k in range(4):
        candidate_hash = 0
        val = 1
        for i in range(5):
            for j in range(5):
                if k == 0:
                    r, s = i, j
                elif k == 1:
                    r, s = 4-j, i
                elif k == 2:
                    r, s = j, 4-i
                else:
                    r, s = 4-i, 4-j

                if matrix[st_x + r][st_y + s]:
                    candidate_hash += val
                val *= 2

        hashes.append(candidate_hash)

    return min(hashes)


def init(N : int, mPlane : List[List[int]]) -> None:
    global plane_n, hash_info, hash_pos_data, prefix_matrix
    plane_n = N
    hash_info = {}
    hash_pos_data = defaultdict(list)
    prefix_matrix = [ [0] * (N+1) for _ in range(N+1) ]

    for i in range(1, N+1):
        for j in range(1, N+1):
            prefix_matrix[i][j] = (
                prefix_matrix[i-1][j] + prefix_matrix[i][j-1]
                + mPlane[i-1][j-1] - prefix_matrix[i-1][j-1]
            )

    # visited = set()

    for row in range(5,N+1):
        col = 5
        while col < (N+1):
            st_row, st_col = row - 5, col - 5
            star_cnt = (
                prefix_matrix[row][col] - prefix_matrix[row-5][col]
                - prefix_matrix[row][col-5] + prefix_matrix[row-5][col-5]
            )
            if star_cnt != 7 or (st_row, st_col) in hash_info:
                col += 1
                continue

            star_hash_val = get_hash(st_row, st_col,mPlane)
            hash_pos_data[star_hash_val].append((st_row, st_col))

            for i in range(st_row, st_row + 5):
                for j in range(st_col, st_col + 5):
                    hash_info[(i,j)] = star_hash_val
            col += 5

    for key in hash_pos_data:
        hash_pos_data[key].sort()


def getCount(mPiece : List[List[int]]) -> int:
    target_hash = get_hash(0,0, mPiece)
    result = len(hash_pos_data[target_hash])
    return result

def getPosition(mRow : int, mCol : int) -> int:
    target_hash = hash_info[(mRow, mCol)]
    target_pos = hash_pos_data[target_hash][0]
    cn_row, cn_col = target_pos[0] + 2, target_pos[1] + 2
    result = (cn_row * 10000) + cn_col
    return result