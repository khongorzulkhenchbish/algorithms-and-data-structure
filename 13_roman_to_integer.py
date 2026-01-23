class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        
        # intuition here is when the i th roman number is less
        # than the i+1 th roman number
        # then we decrease the answer by that, else we increase the ans by that
        roman_sum=0
        for i in range(len(s)):
            if i < len(s) - 1 and roman_map[s[i]] < roman_map[s[i+1]]:
                roman_sum -= roman_map[s[i]]
            else:
                roman_sum += roman_map[s[i]]
        
        return roman_sum