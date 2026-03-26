from heapq import heappop, heappush

class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5

product_info = {}
cate_com_products = [[]]
cate_com_counts = [[]]
cate_com_discount = [[]]

def init() -> None:
    global product_info, cate_com_products, cate_com_discount, cate_com_counts
    product_info = {}
    cate_com_products = [ [list() for _ in range(6)] for _ in range(6) ]
    cate_com_discount = [ [0] * 6 for _ in range(6) ]
    cate_com_counts = [ [0] * 6 for _ in range(6) ]


def sell(mID : int, mCategory : int, mCompany : int, mPrice : int) -> int:
    discount_val = cate_com_discount[mCategory][mCompany]
    product_info[mID] = [mCategory, mCompany, mPrice + discount_val]
    heappush(cate_com_products[mCategory][mCompany], (mPrice + discount_val, mID))
    cate_com_counts[mCategory][mCompany] += 1
    return cate_com_counts[mCategory][mCompany]

def closeSale(mID : int) -> int:
    if mID not in product_info:
        return -1

    cate, com, price = product_info.pop(mID)
    cate_com_counts[cate][com] -= 1

    return price - cate_com_discount[cate][com]

def discount(mCategory : int, mCompany : int, mAmount : int) -> int:
    cate_com_discount[mCategory][mCompany] += mAmount
    discount_val = cate_com_discount[mCategory][mCompany]
    hq = cate_com_products[mCategory][mCompany]

    while hq:
        price, product_id = heappop(hq)
        if product_id not in product_info:
            continue

        cell_price = price - discount_val
        if cell_price <= 0:
            del product_info[product_id]
            cate_com_counts[mCategory][mCompany] -= 1
            continue
        heappush(hq, (price, product_id))
        break

    return cate_com_counts[mCategory][mCompany]

def show(mHow : int, mCode : int) -> RESULT:
    if mHow == 0:
        targets = [ (cate, com) for cate in range(1,6) for com in range(1, 6) ]
    elif mHow == 1:
        targets = [(mCode, com) for com in range(1, 6)]
    else:
        targets = [(cate, mCode) for cate in range(1, 6)]


    candidate_products_list = []

    for cate, com in targets:
        hq = cate_com_products[cate][com]
        discount_val = cate_com_discount[cate][com]
        repair = []
        while hq and len(repair) < 5:
            price, product_id = heappop(hq)
            if product_id not in product_info:
                continue

            cell_price = price - discount_val

            heappush(candidate_products_list, (cell_price, product_id))
            repair.append((price, product_id))

        for price,p_id in repair:
            heappush(hq, (price, p_id))

    cnt = 0
    result = [0, 0, 0, 0, 0]
    while candidate_products_list and cnt < 5:
        price, product_id = heappop(candidate_products_list)
        result[cnt] = product_id
        cnt += 1

    return RESULT(cnt, result)