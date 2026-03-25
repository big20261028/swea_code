from typing import List
from collections import deque, defaultdict

keyword_n = 0
keyword_total = 0
keyword_queue = deque()
keyword_call_cnt = defaultdict(int)


def init(N : int) -> None:
    global keyword_n, keyword_total, keyword_queue, keyword_call_cnt
    keyword_n = N
    keyword_total = 0
    keyword_queue = deque()
    keyword_call_cnt = defaultdict(int)


def addKeyword(mKeyword : str) -> None:
    global keyword_total
    keyword_total += 1
    keyword_queue.append(mKeyword)
    keyword_call_cnt[mKeyword] += 1
    if keyword_total > keyword_n:
    # if len(keyword_queue) > keyword_n:
        dead_word = keyword_queue.popleft()
        keyword_total -= 1
        keyword_call_cnt[dead_word] -= 1
        if keyword_call_cnt[dead_word] == 0:
            del keyword_call_cnt[dead_word]


def top5Keyword(mRet : List[str]) -> int:
    living_words = list(keyword_call_cnt.keys())
    similar_words = defaultdict(list)
    for word in living_words:
        for i in range(len(word)):
            wild_word = word[:i] + '*' + word[i+1:]
            similar_words[wild_word].append(word)
    # print(similar_words)

    parents = { word : word for word in living_words }

    def find_parent(target_word):
        if parents[target_word] == target_word:
            return target_word
        parents[target_word] = find_parent(parents[target_word])
        return parents[target_word]

    def union(a_word, b_word):
        px = find_parent(a_word)
        py = find_parent(b_word)

        if keyword_call_cnt[px] > keyword_call_cnt[py]:
            parents[py] = px
        elif keyword_call_cnt[px] < keyword_call_cnt[py]:
            parents[px] = py
        elif keyword_call_cnt[px] == keyword_call_cnt[py] and px < py:
            parents[py] = px
        elif keyword_call_cnt[px] == keyword_call_cnt[py] and px > py:
            parents[px] = py

        # if keyword_call_cnt[px] > keyword_call_cnt[py]:
        #     parents[py] = px
        # elif keyword_call_cnt[px] == keyword_call_cnt[py] and px < py:
        #     parents[py] = px
        # else:
        #     parents[px] = py

    for words in similar_words.values():
        for i in range(len(words)-1):
            union(words[i], words[i+1])

    candidate_popular_words = defaultdict(int)
    for word in living_words:
        parent_word = find_parent(word)
        candidate_popular_words[parent_word] += keyword_call_cnt[word]

    candidates = sorted(candidate_popular_words, key=lambda x: (-candidate_popular_words[x], x))
    result = candidates[:5]

    for idx in range(len(result)):
        mRet[idx] = result[idx]

    return len(result)
