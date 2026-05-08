from typing import List
from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        1 <= beginWord.length <= 10
        endWord.length == beginWord.length
        1 <= wordList.length <= 5000
        wordList[i].length == beginWord.length
        beginWord, endWord, and wordList[i] consist of lowercase English letters.
        beginWord != endWord
        All the words in wordList are unique.
        """
        word_set = set(wordList) # set look up time O(1)
        if endWord not in word_set:
            return 0

        q = deque()
        q.append((beginWord, 1))
        letters_to_choose_from = set(''.join(wordList)) # max 26

        # Time: O(N*M*26) linear, but N = len(wordList), M = len(word), A = alphabet size tried
        # Space: O(N) N = len(wordList), set + queue + visited behavior
        while q:
            # print(q)
            word, step = q.popleft()
            
            for i in range(len(word)):
                for char in letters_to_choose_from: # O(26)
                    if char == word[i]:
                        continue
                    new_word = word[:i]+char+word[i+1:] # replacing i-th letter
                    if new_word == endWord:
                        return step+1
                    if new_word in word_set: # set: O(1)
                        # BFS
                        q.append((new_word, step+1))
                        word_set.remove(new_word) # set: O(1)
        return 0
        """
        beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"] => 5
        beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"] => 0
        beginWord = "hit", endWord = "hit", wordList = ["hit", "hot"] => 1
        """