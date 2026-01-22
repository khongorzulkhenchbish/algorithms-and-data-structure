class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """ Time: O(N) in the worst case [9999...], Space: O(1)
        The intuition is to do minimal operation as possible. When we iterate backwards,
        we just check if the digit is less than 9, if it is, it means that is the only
        addition we have to do and we can return the digits array early on without
        computing the rest.

        If everything is 9, then we will end up going to the left most and if that is
        gonna be [999] => [1000]

        """
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                # we just add 1 and return immediately
                digits[i] += 1
                return digits
            
            # if the digit is 9, it becomes 10 => 0 and loop continues with carry
            digits[i] = 0

        # if we reach here, it means all digits were 9 (e.g., [9,9,9])
        # the loop turned them all to 0, so we just need to prepend a 1
        return [1] + digits


        # My initial Approach which was simplified later
        carry = 1 # it will be the 1 we add to the last digit

        for i in range(len(digits)-1, -1, -1): # last to first in the digits
            if carry > 0:
                digits[i] += carry
                carry -= 1 # we used our carry
            
            if digits[i] > 9:
                carry = digits[i] // 10
                digits[i] = digits[i] % 10 # assign the last digit
        
        # edge case: [9] => [10] carry = 1   
        if carry > 0:
            digits = [1] + digits
        
        return digits

        # edge case: [8999] => [9 0 0 0] carry = 1   