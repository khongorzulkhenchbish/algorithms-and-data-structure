class Solution:
    def validPalindrome(self, s: str) -> bool:
        # O(n) time, O(1) space
        def helper(left, right):
            while left < right:
                if s[left] == s[right]:
                    left += 1
                    right -= 1
                else:
                    return False # we can't remove 2 or more elements
            return True
        
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                # abaaca: include left - remove right "baa", include right - remove left "aac"
                return helper(left, right-1) or helper(left+1, right)
        
        return True

        """
        abca = a == a => b == c => helper("b") or helper ("c")
        left = 0, 1
        right = 3, 2

        example:
        aba => a == a => stop return True
        left = 0, 1
        right = 2, 1
        """