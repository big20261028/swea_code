import heapq

class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5

id_dict = {}

cate_comp_matrix = []

discount_matrix = []

product_cnt = []


def init() -> None:
    global id_dict, cate_comp_matrix, discount_matrix, product_cnt

    id_dict = {}
    cate_comp_matrix = [ [ [] for _ in range(6) ] for _ in range(6) ]
    discount_matrix = [ [0] * 6 for _ in range(6) ]
    product_cnt = [ [0] * 6 for _ in range(6) ]

def sell(mID : int,
         mCategory : int,
         mCompany : int,
         mPrice : int) -> int:

    discount = discount_matrix[mCategory][mCompany]
    price = mPrice + discount
    id_dict[mID] = [mCategory,mCompany, price]
    heapq.heappush(cate_comp_matrix[mCategory][mCompany],(price,mID))
    product_cnt[mCategory][mCompany] += 1

    return product_cnt[mCategory][mCompany]

def closeSale(mID : int) -> int:
    if mID not in id_dict:
        return -1

    cate,com,price = id_dict.pop(mID)
    product_cnt[cate][com] -= 1

    return price - discount_matrix[cate][com]

def discount(mCategory : int,
             mCompany : int,
             mAmount : int) -> int:
    discount_matrix[mCategory][mCompany] += mAmount
    discount = discount_matrix[mCategory][mCompany]
    products_heap = cate_comp_matrix[mCategory][mCompany]

    while products_heap:
        price, m_id = heapq.heappop(products_heap)
        if m_id not in id_dict:
            continue
        sell_price = price - discount

        if sell_price <= 0 :
            del id_dict[m_id]
            product_cnt[mCategory][mCompany] -= 1
        else:
            heapq.heappush(products_heap,(price,m_id))
            break

    return product_cnt[mCategory][mCompany]

def show(mHow : int,
         mCode : int) -> RESULT:
    result_cnt = 0
    result_ids = [0] * 5

    if mHow == 0:
        targets = [ (cate,comp) for cate in range(1,6) for comp in range(1,6) ]
    elif mHow == 1:
        targets = [(mCode, comp) for comp in range(1, 6)]
    elif mHow == 2:
        targets = [(cate, mCode) for cate in range(1, 6)]

    candidate_list = []
    for cate,comp in targets:
        product_heap = cate_comp_matrix[cate][comp]
        repair = []
        cnt = 0
        while product_heap and cnt < 5:
            price, m_id = heapq.heappop(product_heap)
            if m_id not in id_dict:
                continue
            repair.append((price, m_id))
            sell_price = price - discount_matrix[cate][comp]
            heapq.heappush(candidate_list,(sell_price,m_id))
            cnt += 1

        for data in repair:
            heapq.heappush(product_heap,data)

    idx = 0
    while candidate_list and idx < 5:
        sell_price, m_id = heapq.heappop(candidate_list)
        result_ids[idx] = m_id
        idx += 1
    result_cnt = idx

    return RESULT(result_cnt, result_ids)