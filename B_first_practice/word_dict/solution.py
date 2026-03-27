from bisect import bisect_left

class PAGE:
    def __init__(self, no, word):
        self.no = no
        self.word = word

words = []
trie_root = {}
word_map = {}
cur_page = 0
registered_cnt = 0


def init() -> None:
    global words, trie_root, word_map, cur_page, registered_cnt
    words = []
    trie_root = {}
    word_map = {}
    cur_page = 0
    registered_cnt = 0
    add('a', 1)


def add(mWord : str, mImportance : int) -> PAGE:
    global cur_page, registered_cnt
    insert_idx = bisect_left(words, mWord)
    words.insert(insert_idx, mWord)
    registered_cnt += 1
    word_map[mWord] = (mImportance, registered_cnt)

    trie = trie_root
    for c in mWord:
        if c not in trie:
            trie[c] = {'best' : mWord}
        else:
            cur_best = trie[c]['best']
            cur_importance, cur_registered_cnt = word_map[cur_best]
            if mImportance > cur_importance or (mImportance == cur_registered_cnt and registered_cnt < cur_registered_cnt):
                trie[c]['best'] = mWord
        trie = trie[c]
    cur_page = insert_idx + 1

    return PAGE(cur_page, mWord)

def move(mDir : int) -> PAGE:
    global  cur_page
    cur_page += mDir
    return PAGE(cur_page, words[cur_page-1])

def search(mStr : str) -> PAGE:
    global cur_page
    if mStr in word_map:
        cur_page = bisect_left(words, mStr) + 1
        return PAGE(cur_page, mStr)

    trie = trie_root
    for c in mStr:
        if c not in trie:
            return PAGE(-1, mStr)
        trie = trie[c]
    best_word = trie['best']
    cur_page = bisect_left(words, best_word) + 1
    return PAGE(cur_page, best_word)

    return PAGE(-1, "")

def go(mNo : int) -> PAGE:
    return PAGE(-1, "")