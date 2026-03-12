from heapq import heappush, heappop

class RESULT:
    def __init__(self, cnt, IDs):
        self.cnt = cnt
        self.IDs = IDs  # [int] * 5

products_matrix = [[]] # [cate][com] = [ (price, id), (price, id), (price, id) .... ] 우선순위 큐 쓰기
discount_matrix = [[]] # [cate][com] = 할인률
products_id = {} # 상품아이디 : (가격, 품목, 제조사)
products_cnt = [[]] # [cate][com] = 상품개수

def init() -> None:
    global products_id, products_matrix, discount_matrix, products_cnt
    products_matrix = [ [ [] for _ in range(6) ] for _ in range(6)] # 바로 인덱스로 접근할 수 있도록 0 ~ 5
    discount_matrix = [ [0] * 6 for _ in range(6) ]
    products_cnt = [ [0] * 6 for _ in range(6) ]
    products_id.clear()


def sell(mID : int, mCategory : int, mCompany : int, mPrice : int) -> int:
    sum_prise = mPrice + discount_matrix[mCategory][mCompany]

    products_id[mID] = (sum_prise, mCategory, mCompany)
    heappush(products_matrix[mCategory][mCompany], (sum_prise, mID))
    products_cnt[mCategory][mCompany] += 1

    return products_cnt[mCategory][mCompany]

def closeSale(mID : int) -> int:
    if mID not in products_id:
        return -1

    price, cate, com = products_id.pop(mID)
    products_cnt[cate][com] -= 1

    return price - discount_matrix[cate][com]


def discount(mCategory : int, mCompany : int, mAmount : int) -> int:
    discount_matrix[mCategory][mCompany] += mAmount
    dis_val = discount_matrix[mCategory][mCompany]

    hq = products_matrix[mCategory][mCompany]
    while hq:
        price, p_id = heappop(hq)
        if p_id not in products_id:
            continue

        if price <= dis_val:
            del products_id[p_id]
            products_cnt[mCategory][mCompany] -= 1
            continue
        else:
            heappush(hq, (price,p_id))
            break

    return products_cnt[mCategory][mCompany]

def show(mHow : int, mCode : int) -> RESULT:
    if mHow == 0:
        targets = [ (cate,com) for cate in range(1,6) for com in range(1,6)]
    elif mHow == 1:
        targets = [(mCode, com) for com in range(1, 6)]
    elif mHow == 2:
        targets = [(cate, mCode) for cate in range(1, 6)]

    cheap_products = [] # 힙큐로 관리

    for cate,com in targets:
        hq = products_matrix[cate][com]
        repair = []
        while hq and len(repair) < 5:
            price, p_id = heappop(hq)
            if p_id not in products_id:
                continue

            real_price = price - discount_matrix[cate][com]
            if real_price <= 0:
                continue

            heappush(cheap_products, (real_price, p_id))
            repair.append((price, p_id))

        for price, p_id in repair:
            heappush(hq, (price, p_id))

    cheap_ids = []
    while cheap_products and len(cheap_ids) < 5:
        price, p_id = heappop(cheap_products)
        cheap_ids.append(p_id)

    cnt = 0
    result = [0, 0, 0, 0, 0]
    for idx,p_id in enumerate(cheap_ids):
        result[idx] = p_id
        cnt += 1

    return RESULT(cnt, result)