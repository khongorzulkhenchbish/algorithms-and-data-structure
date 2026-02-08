class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''
        https://web.stanford.edu/class/cs124/lec/med.pdf
        In Natural Language Processing - distance between words
        In Computational Biology - genetic alignment

        a|cd and a|bd
        if word1[i] == word2[i] then we have a subproblem.

        ac|d and ab|d
        if word1[i] != word2[i] then we have 3 options:
        - insert - (i, j+1)
        - delete - (i+1, j)
        - replace - (i+1, j+1)

        if we end up at "" and "" then the base case is 0 for these.
        
        Bottom up table
        Time: O(M*N), Space: O(M*N)
            |  a  |  c  |  d  |  "" |
        a   |  1  |  2  |  2  |  3  |  
        b   |  2  |  1  |  1  |  2  |  
        d   |  2  |  1  |  0  |  1  |  
        ""  |  3  |  2  |  1  |  0  |
        By the time it reaches a and a, the min operation to convert
        abd into acd will be 1.
        '''
        rows = len(word1)
        cols = len(word2)

        cache = [[float("INF")] * (cols+1) for i in range(rows + 1)]

        # init base case for the 2d array, last row and last column
        for j in range(cols + 1):
            cache[rows][j] = cols - j
        for i in range(rows + 1):
            cache[i][cols] = rows - i
        
        # print(cache)
        # [
        #     [inf, inf, inf, 5],
        #     [inf, inf, inf, 4], 
        #     [inf, inf, inf, 3], 
        #     [inf, inf, inf, 2], 
        #     [inf, inf, inf, 1], 
        #     [3,   2,   1,   0]
        # ]

        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1]
                else:
                    # min of 3 choice
                    cache[i][j] = 1 + min(cache[i+1][j], cache[i][j+1], cache[i+1][j+1])
        
        return cache[0][0]