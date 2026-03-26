from typing import List

from collections import defaultdict, deque

word_n = 0
word_queue = deque()
word_call_cnt = defaultdict(int)
capacity = 0

def init(N : int) -> None:
    global word_n, word_queue, word_call_cnt, capacity
    word_n = N
    word_queue = deque()
    word_call_cnt = defaultdict(int)
    capacity = 0


def addKeyword(mKeyword : str) -> None:
    global capacity
    word_queue.append(mKeyword)
    word_call_cnt[mKeyword] += 1
    capacity += 1
    if capacity > word_n:
        capacity -= 1
        dead_word = word_queue.popleft()
        word_call_cnt[dead_word] -= 1
        if word_call_cnt[dead_word] == 0:
            del word_call_cnt[dead_word]


def top5Keyword(mRet : List[str]) -> int:
    living_words = [ word for word in word_call_cnt ]

    similar_words = defaultdict(list)
    for word in living_words:
        for i in range(len(word)):
            wild_word = word[:i] + '*' + word[i+1:]
            similar_words[wild_word].append(word)

    parents = { word : word for word in living_words }

    def find_parent(word):
        if word == parents[word]:
            return word
        parents[word] = find_parent(parents[word])
        return parents[word]

    def union(a_word, b_word):
        pa = find_parent(a_word)
        pb = find_parent(b_word)

        if word_call_cnt[pa] > word_call_cnt[pb] or (word_call_cnt[pa] == word_call_cnt[pb] and pa < pb):
            parents[pb] = pa
        else:
            parents[pa] = pb

    for words in similar_words.values():
        for i in range(len(words) - 1):
            union(words[i], words[i+1])

    popular_words_dict = defaultdict(int)
    for word in living_words:
        parent = find_parent(word)
        popular_words_dict[parent] += word_call_cnt[word]

    sorted_data = sorted(popular_words_dict, key= lambda x : (-popular_words_dict[x], x))
    result = sorted_data[:5]

    for idx, word in enumerate(result): # 키값이 단어
        mRet[idx] = word

    return len(result)
