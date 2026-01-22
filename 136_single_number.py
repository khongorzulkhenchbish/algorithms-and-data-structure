class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """ Time: O(N), Space: O(1)
        4 ...100
        1 ...001
        2 ...010
        1 ...001
        2 ...010
        If we use exclusive or "XOR", which returns 1^1=>0, 0^1 or 1^0=>0, 0^0=>0
        for same values 2,2 => 010^010=>000 CANCELS OUT
        """
        # 4,1,2,1,2
        answer = 0

        for num in nums:
            answer = answer ^ num

        return answer