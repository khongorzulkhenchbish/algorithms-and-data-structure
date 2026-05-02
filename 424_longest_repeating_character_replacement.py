class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        Time complexity: O(n)
        Space complexity: O(m) which is at most 26 so the space is constant
        Where n is the length of the string and m is the total number of unique characters in the string.
        A|BABB|AA => {A:4, B:3}
        '''
        count = {}
        maxLen = 0
        
        left = 0
        maxfreq = 0
        for right in range(len(s)):
            letter = s[right]
            count[letter] = 1 + count.get(letter, 0) # if it is not in the count map then add it as {"letter":0}
            maxfreq = max(maxfreq, count[letter]) # we need to set it at every iteration

            # if the number of chars that needs to change exceeds K
            while ((right - left + 1) - maxfreq) > k:
                count[s[left]] -= 1 # remove elem from the left
                left+= 1            # move the sliding window
            
            maxLen = max(maxLen, right - left + 1)

        return maxLen
        '''
        ABAB, k=2
        left    right   count       maxfreq     right-left+1    maxlen  substr
        0       0       {A:1}       1           0-0+1           1       A
        0       1       {A:1, B:1}  1           1-0+1           2       AB
        0       2       {A:2, B:1}  2           2-0+1           3       ABA
        0       3       {A:2, B:2}  2           3-0+1           4       ABAB
        return maxlen=4

        AABABBA, k=1
        left    right   count       maxfreq     right-left+1    maxlen  substr
        0       0       {A:1}       1           0-0+1           1       A
        0       1       {A:2}       2           1-0+1           2       AA
        0       2       {A:2, B:1}  2           2-0+1           3       AAB
        0       3       {A:3, B:1}  3           3-0+1           4       AABA
        0       4       {A:3, B:2}  3           4-0+1=>AABAB=>5-3>k     remove from the left side.
        1               {A:2, B:2}              4-1+1=> ABAB=>4-3=k  4, ABAB
        1       5       {A:2, B:3}  3           5-1+1=>ABABB=>5-3>k     remove from the left side.
        2               {A:1, B:3}              5-2+1=> BABB=>4-3=k  4, BABB
        2       6       {A:2, B:3}  3           6-2+1=>BABBA=>4-3>k     remove from the left side
        3               {A:2, B:2}              6-3+1=> ABBA=>4-3>k  4, ABBA
        return maxLen=4
        '''