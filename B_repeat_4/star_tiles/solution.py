from typing import List

from collections import defaultdict

plane_n = 0
pos_hash_info = {} # pos_hash_info[(x,y)] = hash_val
hash_pos_data = defaultdict(list) # hash_pos_data[hash_val] = [ (x,y), (x,y) .... ]
prefix_matrix = [[]]

def get_hash(x, y, matrix):
    hash_val_list = []
    for k in range(4):
        hash_val = 0
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

                if matrix[x+r][y+s] == 1:
                    hash_val += val
                val *= 2

        hash_val_list.append(hash_val)
    return min(hash_val_list)


def init(N : int, mPlane : List[List[int]]) -> None:
    global plane_n, pos_hash_info, hash_pos_data, prefix_matrix
    plane_n = N
    pos_hash_info = {}
    hash_pos_data = defaultdict(list)
    prefix_matrix = [ [0] * (N+1) for _ in range(N+1)]

    for i in range(1, N+1):
        for j in range(1, N+1):
            prefix_matrix[i][j] = (
                prefix_matrix[i-1][j] + prefix_matrix[i][j-1]
                + mPlane[i-1][j-1] - prefix_matrix[i-1][j-1]
            )

    for row in range(5,N+1):
        col = 5
        while col < (N+1):
            st_row, st_col = row - 5, col - 5
            star_cnt = (
                prefix_matrix[row][col] - prefix_matrix[row-5][col]
                - prefix_matrix[row][col-5] + prefix_matrix[row-5][col-5]
            )
            if star_cnt != 7 or (st_row, st_col) in pos_hash_info:
                col += 1
                continue

            hash_val = get_hash(st_row, st_col, mPlane)
            hash_pos_data[hash_val].append((st_row, st_col))

            for i in range(st_row, st_row + 5):
                for j in range(st_col, st_col + 5):
                    pos_hash_info[(i,j)] = hash_val

            col += 5

    for key in hash_pos_data:
        hash_pos_data[key].sort()


def getCount(mPiece : List[List[int]]) -> int:
    target_hash = get_hash(0,0, mPiece)
    result = len(hash_pos_data[target_hash])
    return result

def getPosition(mRow : int, mCol : int) -> int:
    target_hash = pos_hash_info[(mRow,mCol)]
    row, col = hash_pos_data[target_hash][0]
    center_r, center_c = row + 2, col + 2
    result = (center_r * 10000) + center_c
    return result