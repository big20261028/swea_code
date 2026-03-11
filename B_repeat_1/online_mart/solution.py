#import heapq
from heapq import heappop,heappush,heapify

class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5

id_dict = {} # id : (price, cate, com)
cate_com_matrix = [ [ list() for _ in range(6) ] for _ in range(6) ] # [cate][com] = heapq
discount_matrix = [ [0] * 6 for _ in range(6) ] # [cate][com] = int
product_cnt = [ [0] * 6 for _ in range(6) ] # [cate][com] = int

def init() -> None:
    global id_dict, cate_com_matrix, discount_matrix, product_cnt

    id_dict.clear()  # id : (price, cate, com)
    cate_com_matrix = [[list() for _ in range(6)] for _ in range(6)]  # [cate][com] = heapq
    discount_matrix = [[0] * 6 for _ in range(6)]  # [cate][com] = int
    product_cnt = [[0] * 6 for _ in range(6)]  # [cate][com] = int

def sell(mID : int,
         mCategory : int,
         mCompany : int,
         mPrice : int) -> int:

    id_dict[mID] = (mCategory,mCompany,mPrice + discount_matrix[mCategory][mCompany])
    heappush(cate_com_matrix[mCategory][mCompany], (mPrice + discount_matrix[mCategory][mCompany], mID))
    product_cnt[mCategory][mCompany] += 1

    return product_cnt[mCategory][mCompany]

def closeSale(mID : int) -> int:
    if mID not in id_dict:
        return -1
    del_data = id_dict.pop(mID)
    product_cnt[del_data[0]][del_data[1]] -= 1
    return del_data[2] - discount_matrix[del_data[0]][del_data[1]]

def discount(mCategory : int,
             mCompany : int,
             mAmount : int) -> int:

    discount_matrix[mCategory][mCompany] += mAmount
    hq = cate_com_matrix[mCategory][mCompany]

    while hq:
        price, Mid = heappop(hq)
        if Mid not in id_dict:
            continue

        if price <= discount_matrix[mCategory][mCompany]:
            product_cnt[mCategory][mCompany] -= 1
            del id_dict[Mid]
        else:
            heappush(hq,(price,Mid))
            break

    return product_cnt[mCategory][mCompany]


def show(mHow : int,
         mCode : int) -> RESULT:
    rs_cnt, rs_list = 0, [0] * 5

    if mHow == 0:
        target_pos = [ (row,col) for row in range(1,6) for col in range(1,6) ]
    elif mHow == 1:
        target_pos = [ (mCode,col) for col in range(1,6) ]
    elif mHow == 2:
        target_pos = [ (row, mCode) for row in range(1,6) ]

    candidate_hq = []

    for cate,com in target_pos:
        hq = cate_com_matrix[cate][com]
        repair = []
        cnt = 0
        while hq and cnt < 5:
            price, Mid = heappop(hq)
            if Mid not in id_dict:
                continue

            heappush(candidate_hq, (price - discount_matrix[cate][com], Mid))
            repair.append((price,Mid))
            cnt +=1

        for price, mid in repair:
            heappush(hq, (price,mid))

    #print(candidate_hq)

    result = []
    while candidate_hq and len(result) < 5:
        price,mid = heappop(candidate_hq)
        result.append(mid)

    for i in range(len(result)):
        rs_cnt += 1
        rs_list[i] = result[i]

    return RESULT(rs_cnt, rs_list)