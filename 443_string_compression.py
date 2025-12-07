class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Time: O(N), Space: O(1)
        """
        
        length = len(chars)
        left = 0
        count = 1 # because if the freq is 1, we don't add the count

        for right in range(1, length+1):
            # right = {0,1,2,3,4,5,6}
            if right < length and chars[right] == chars[right-1]:
                count += 1
            else:
                # different char found or the right length reached, therefore save the prev's freq
                chars[left] = chars[right-1] # update the char
                left += 1                   # updates only when the current writw is written
                if count > 1:
                    # the frequency can be 2 digits
                    for digit in str(count):
                        # we should add the count or the next char next time
                        chars[left] = digit
                        left += 1
                count = 1
        # return the end of the updated range or the len of the abbrebiated string
        return left
        """
        Example 1. chars = ["a","2","b","2","c","c","c"]
        left = 
        right = 
        count = 
        """
