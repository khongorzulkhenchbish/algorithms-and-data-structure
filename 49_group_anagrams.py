class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group = collections.defaultdict(list)
        
        for word in strs:
            freq = [0]*26
            for char in word:
                freq[ord(char)-ord('a')] += 1
            group[tuple(freq)].append(word)
        return group.values() 

