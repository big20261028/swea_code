from typing import List
from collections import defaultdict, deque

# 검색어 개수
n = 0
# 검색어 목록
words_list = deque()
# 검색어 전달 횟수
words_call_cnts = defaultdict(int)

def init(N : int) -> None:
    global n, words_list, words_call_cnts
    n = N
    words_list = deque()
    words_call_cnts = defaultdict


def addKeyword(mKeyword : str) -> None:
    words_list.append(mKeyword)
    words_call_cnts[mKeyword] += 1

    if len(words_list) > n:
        dead_word = words_list.popleft()
        words_call_cnts[dead_word] -= 1
        if words_call_cnts[dead_word] == 0:
            del words_call_cnts[dead_word]


def top5Keyword(mRet : List[str]) -> int:

    words = []
    for word in words_call_cnts:
        words.append(word)

    similar_words_list = defaultdict(list)
    for word in words:
        for i in range(len(word)):
            wild_word = word[:i] + '*' + word[i+1:]
            similar_words_list[wild_word].append(word)

    parent = { word:word for word in words }

    def find_parent(node):
        if parent[node] == node:
            return node
        parent[node] = find_parent(parent[node])
        return parent[node]

    def union(node_a, node_b):
        px = find_parent(node_a)
        py = find_parent(node_b)

        if words_call_cnts[px] > words_call_cnts[py]:
            parent[py] = px
        elif words_call_cnts[px] == words_call_cnts[py] and px < py:
            parent[py] = px
        else:
            parent[px] = py

    for similar_words in similar_words_list.values():
        for i in range(len(similar_words)-1):
            union(similar_words[i], similar_words[i+1])

    popular_words = defaultdict(int)
    for word in words:
        parent = find_parent(word)
        popular_words[parent] += words_call_cnts[word]

    sort_data = sorted(popular_words.keys(), key= lambda x : (-popular_words[x], x))
    result = sort_data[:5]

    for i, word in enumerate(result):
        mRet[i] = result[i]

    return len(result)
