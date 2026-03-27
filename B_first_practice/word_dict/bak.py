class PAGE:
    def __init__(self, no, word):
        self.no = no
        self.word = word


class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0
        self.end_count = 0
        self.best_word = ""


root = TrieNode()
word_map = {}  # word_map[단어] = (중요도, 등록번호)
cur_page = 0  # 현재 페이지
registered_cnt = 0  # 누적 등록 횟수


def init() -> None:
    global root, word_map, cur_page, registered_cnt
    root = TrieNode()
    word_map = {}
    cur_page = 0
    registered_cnt = 0
    add('a', 1)


def is_better(new_word, old_word):
    if not old_word:
        return True
    new_import, new_page = word_map[new_word]
    old_import, old_page = word_map[old_word]

    if new_import > old_import:
        return True
    if new_import == old_import and new_page < old_page:
        return True
    return False


def get_rank(word):
    rank = 0
    curr = root
    for char in word:
        if curr.end_count > 0:
            rank += curr.end_count

        for c in sorted(curr.children.keys()):  # children에 등록된 키들 가져오기
            if c < char:  # char보다 사전순으로 앞선것만 확인
                rank += curr.children[c].count
            else:
                break
        curr = curr.children[char]
        # 마지막 char의 조사 마친 후 for문 종료됨
        # 고로, char의 개수가 추가되지 않음
    return rank


def get_word_by_rank(k):
    curr = root
    word_chars = []

    while k > 0:
        if curr.end_count > 0:
            if k <= curr.end_count:  # k가 찾는 순서의 단어일경우
                return ''.join(word_chars)
        k -= curr.end_count

        for c in sorted(curr.children.keys()):
            child = curr.children[c]
            if k > child.count:
                k -= child.count
            else:
                word_chars.append(c)
                curr = child
                break
    # 방어코드
    # 거의실행되지 않음
    return ''.join(word_chars)


def add(mWord: str, mImportance: int) -> PAGE:
    global cur_page, registered_cnt

    registered_cnt += 1  # 등록된 순서
    word_map[mWord] = (mImportance, registered_cnt)  # 중요도, 등록된 순서 저장

    curr = root
    curr.count += 1

    for char in mWord:
        if char not in curr.children:
            curr.children[char] = TrieNode()
        curr = curr.children[char]
        curr.count += 1

        if is_better(mWord, curr.best_word):
            curr.best_word = mWord

    curr.end_count += 1

    cur_page = get_rank(mWord) + 1
    return PAGE(cur_page, mWord)


def move(mDir: int) -> PAGE:
    global cur_page
    cur_page += mDir
    word = get_word_by_rank(cur_page)
    return PAGE(cur_page, word)


def search(mStr: str) -> PAGE:
    global cur_page

    if mStr in word_map:
        cur_page = get_rank(mStr) + 1
        return PAGE(cur_page, mStr)

    curr = root
    for char in mStr:
        if char not in curr.children:
            return PAGE(-1, mStr)
        curr = curr.children[char]

    best_word = curr.best_word
    cur_page = get_rank(best_word) + 1
    return PAGE(cur_page, best_word)

    return PAGE(-1, "")


def go(mNo: int) -> PAGE:
    global cur_page
    cur_page = mNo
    word = get_word_by_rank(cur_page)
    return PAGE(cur_page, word)