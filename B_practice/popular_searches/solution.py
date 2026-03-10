from typing import List
from collections import deque, defaultdict

n = 0
words = deque()
word_cnt = defaultdict(int)

def init(N : int) -> None:
    global n, words, word_cnt
    n = N
    words = deque()
    word_cnt = defaultdict(int)

def addKeyword(mKeyword : str) -> None:
    words.append(mKeyword)
    word_cnt[mKeyword] += 1

    if len(words) > n:
        dead_word = words.popleft()
        word_cnt[dead_word] -= 1
        if word_cnt[dead_word] == 0:
            del word_cnt[dead_word]

def top5Keyword(mRet : List[str]) -> int:
    word_list = list(word_cnt.keys())

    similar_word = defaultdict(list)

    for word in word_list:
        for i in range(len(word)):
            wild_word = word[:i] + '*' + word[i+1:]
            similar_word[wild_word].append(word)

    parent_data = { word : word for word in word_list }

    def find_parent(word):
        if word == parent_data[word]:
            return word
        parent_data[word] = find_parent(parent_data[word])
        return parent_data[word]

    def union(a_word, b_word):
        px = find_parent(a_word)
        py = find_parent(b_word)

        # 많이 전달된 순
        # 같다면, 사전순
        if word_cnt[px] > word_cnt[py] or (word_cnt[px] == word_cnt[py] and px < py):
            parent_data[py] = px
        else:
            parent_data[px] = py

    for sm_word in similar_word.values():
        for i in range(len(sm_word)-1):
            union(sm_word[i],sm_word[i+1])

    popular_words = defaultdict(int)
    for word in word_list:
        parent_word = find_parent(word)
        popular_words[parent_word] += word_cnt[word]

    #print(popular_words)
    rank = sorted(popular_words.keys(), key= lambda word : (-popular_words[word],word))
    result = rank[:5]
    for idx, word in enumerate(result):
        mRet[idx] = word

    return len(result)
