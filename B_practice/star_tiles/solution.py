from typing import List
from collections import defaultdict

hash_pos = defaultdict(list)
n = 0
prefix_matrix = [[]]
pos_hash = {}

binary_list = [1]
for i in range(1,25):
    binary_list.append(binary_list[i-1] * 2)

def get_hash(row,col,matrix):
    hash_data = []
    for k in range(4):
        hash_val = 0
        idx = 0
        for i in range(5):
            for j in range(5):
                if k == 0:
                    r, c = i, j
                elif k == 1:
                    r, c = 4-j, i
                elif k == 2:
                    r, c = 4-i, 4-j
                elif k == 3:
                    r, c = j, 4-i

                if matrix[row + r][col + c] != 0:
                    hash_val += binary_list[idx]
                idx += 1
        hash_data.append(hash_val)
    return min(hash_data)

def init(N : int, mPlane : List[List[int]]) -> None:
    global hash_pos, n, prefix_matrix, pos_hash
    hash_pos = defaultdict(list)
    n = N
    prefix_matrix = [ [0] * (N+1) for _ in range(N+1) ]

    for i in range(1,N+1):
        for j in range(1,N+1):
            prefix_matrix[i][j] = (
                prefix_matrix[i-1][j] + prefix_matrix[i][j-1] + mPlane[i-1][j-1] - prefix_matrix[i-1][j-1]
            )

    tile_pos = []
    visited = set()

    for row in range(5,N+1):
        col = 5
        while col <= N:
            start_row, start_col = row-4, col-4
            prefix_val = (
                prefix_matrix[row][col] - prefix_matrix[row-5][col]
                - prefix_matrix[row][col-5] + prefix_matrix[row-5][col-5]
            )
            if (start_row, start_col) in visited or prefix_val != 7:
                col += 1
                continue

            for i in range(start_row, start_row+5):
                for j in range(start_col, start_col+5):
                    visited.add((i,j))
            tile_pos.append((start_row,start_col))
            col += 5

    for pos in tile_pos:
        row = pos[0] - 1
        col = pos[1] - 1
        hash_key = get_hash(row,col,mPlane)
        hash_pos[hash_key].append((row,col))
        for i in range(row, row+5):
            for j in range(col, col+5):
                pos_hash[(i,j)] = hash_key

    for key in hash_pos:
        hash_pos[key].sort()


def getCount(mPiece : List[List[int]]) -> int:
    hash_key = get_hash(0,0,mPiece)
    return len(hash_pos[hash_key])

def getPosition(mRow : int, mCol : int) -> int:
    hash_key = pos_hash[(mRow, mCol)]
    target_tile = hash_pos[hash_key][0]
    r = target_tile[0] + 2
    c = target_tile[1] + 2
    result = (r * 10000) + c
    return result