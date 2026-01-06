class Solution:
    def longest_subs(self, s: str, left: int, right: int):
        while left>=0 and right<len(s) and s[left]==s[right]:
            left-=1
            right+=1
        else: # "acd" then only c is the palindrome, left and right pointers should be reverted once
            left+=1
            right-=1
            return s[left:right+1]

    def longestPalindrome(self, s: str) -> str:
        """ Intuition is to assume every character is the mid element then expand to the left
        and right at the same time "as long as we can go". Then length can be determined by
        the index difference.
        This is way better than finding the leftmost and rightmost characters first then 
        shrink approach, because we don't know how that will go if "acccajk".

        No matter if the given string is even or odd length, the palindrom itself has either
        even, odd length.

        Time: O(N*(N for worst, N/2 at best)), Space: O(1)
        """
        maxs=""
        for i in range(len(s)):
            # 1. compute odd case, like "aba", then update maxstring if odd legth palindrome is longer
            odd = self.longest_subs(s, i, i)
            if len(odd) > len(maxs):
                maxs=odd
            # 2. compute even case, like "abba", then update maxstring if even length palindrom is longer
            even = self.longest_subs(s, i, i+1)
            if len(even) > len(maxs):
                maxs=even
        
        return maxs