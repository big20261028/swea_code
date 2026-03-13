from typing import List
from collections import defaultdict, deque
from heapq import heappush, heappop

max_n = 0
keyword_list = deque()
word_call_cnt = defaultdict(int)


def init(N : int) -> None:
    global max_n, keyword_list, word_call_cnt
    max_n = N
    keyword_list = deque()
    word_call_cnt = defaultdict(int)


def addKeyword(mKeyword : str) -> None:
    keyword_list.append(mKeyword)
    word_call_cnt[mKeyword] += 1

    if len(keyword_list) > max_n:
        dead_word = keyword_list.popleft()
        word_call_cnt[dead_word] -= 1
        if word_call_cnt[dead_word] == 0:
            del word_call_cnt[dead_word]


def top5Keyword(mRet : List[str]) -> int:
    target_words = [ keyword for keyword in word_call_cnt ]
    #print(target_words)

    similar_words = defaultdict(list)

    for word in target_words:
        for i in range(len(word)):
            wild_word = word[:i] + '*' + word[i+1:]
            similar_words[wild_word].append(word)

    parents = { word: word for word in target_words }

    # print(similar_words)
    # print(parents)

    def find_parent(node):
        if parents[node] == node:
            return node
        parents[node] = find_parent(parents[node])
        return parents[node]

    def union(word1, word2):
        mx = find_parent(word1)
        my = find_parent(word2)

        if word_call_cnt[mx] > word_call_cnt[my]:
            parents[my] = mx
        elif word_call_cnt[mx] == word_call_cnt[my] and mx < my:
            parents[my] = mx
        else:
            parents[mx] = my

    for word_list in similar_words.values():
        for i in range(len(word_list)-1):
            union(word_list[i],word_list[i+1])

    popular_words = defaultdict(int)
    for word in target_words:
        parent = find_parent(word)
        popular_words[parent] += word_call_cnt[word]

    #print(popular_words)

    sort_keywords = sorted(popular_words, key=lambda x : (-(popular_words[x]), x))
    #print(sort_keywords)
    result = sort_keywords[:5]
    for idx, word in enumerate(result):
        mRet[idx] = word

    return len(result)
