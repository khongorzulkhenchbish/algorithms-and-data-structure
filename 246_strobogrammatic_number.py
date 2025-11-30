class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        # Time: O(N), Space: O(1) only stores the stro numbers
        # The idea is to think that 180 rotated version is the swapped version of the string from both sides.
        # Therefore, instead of checking the equality, checking if the other side is equal to the "rotated version" of it.
        stromap = {"9":"6", "6":"9", "8":"8", "0":"0", "1":"1"}
        left = 0
        right = len(num)-1

        while(left <= right):
            if stromap.get(num[left], -1) == num[right]:
                left += 1
                right -= 1
            else:
                return False
        
        return True
        # "69" => stromap[6] = 9 == 9 => true, left = 1, right = 0, return True
        # "962" => stromap[9] = (6 == 2) => false
