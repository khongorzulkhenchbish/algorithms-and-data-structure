class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # "tmabmzuxt" = 7 because "abmxuzt"
        #  left is for sticking, it doesn't change unless repeated string appears.
        #  right is for iterating through as far as possible.
        #  the length of the longest string will be "right-left+1"
        #  occurred = {"the character" : "always pointing to the next index of the char."}
        #  Time: O(N) visits every char once    Space: O(26) if all chars are unique 
        maxLen = 0
        occurred={}
        left=0
        for right in range(len(s)):
            if s[right] in occurred:
                left=max(occurred[s[right]], left)
        
            maxLen=max(maxLen, right-left+1)
            occurred[s[right]]=right+1
            
        return maxLen
        """ s = tmabmzuxt
        occurred = {t:1, m:2, a:3, b:4} => {t:1, m:5, a:3, b:4, z:5, u:6, x:7}
        left = 0, max(2,0)=2, 
        right = 0, 1, 2, 3, 4, 5, 6, 7, 8
        maxLen = 1, 2, 3, 4, max(4,3)=4, 4, 5, 6, 7 => 
        maxS = t, tm, tma, tmab, abm, abmz, abmzu, abmzux, "ambzuxt" 
        """