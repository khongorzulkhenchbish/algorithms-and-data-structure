class Solution:
    def makeGood(self, s: str) -> str:
        '''
        I'd propose a two pointer approach that runs recursively as brute force approach.
        I would define a recursive helper function that takes str.
        We use left and right pointer until we find lower(left) == lower(right),
        then if left-1 is greater, equal than 0, then we call helper(str[:left]+str[right+1:])
        else when left is less than zero, we call helper(str[right:])

        if we end finding no left and right equal situation, we return that substring.

        Time: O(N^2) because AaAaAa..., you perform O(N) slices for each time.
        Space: O(N^2) in the worst case where everything ends up eliminated.

        Q1: Can this be optimized using data structure?
        Yes, using stack to cancel out the last appeared adjacent chars.

        Time: O(N) as every char is pushed and popped once.
        Space: O(N) if there is no adjacent chars, we end up saving N length of chars.

        Constraint: 1 <= s.length <= 100
        '''

        stack = []

        for char in s:
            # abs(ord('a') - ord('A')) is always 32
            if stack and abs(ord(stack[-1]) - ord(char)) == 32:
                stack.pop() # cancel out the "eE" in "l(eE)eetcode"
            else:
                # either stack empty, or the char doesn't equal
                stack.append(char)
        
        return "".join(stack)

        # Example 1:
        # s = "a" => stack=[a]

        # Example 2:
        # s = "abBAcC" => 
        # stack=[a,b] => [a] = [] = [c] = []
        # char = B    =>  A  = c  = C

# Follow up 1: Can you write some unit test cases for your solution. Think it as if you are designing a feature.
import unittest

class TestMakeGood(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def happy_path_test(self):
        self.assertEqual(self.sol.makeGood("leEeetcode"), "leetcode")
        self.assertEqual(self.sol.makeGood("aA"), "")
        # The removal of 'bB' creates the new bad pair 'aA', removal of distant pairs
        self.assertEqual(self.sol.makeGood("abBA"), "")

    def test_empty_input(self):
        self.assertEqual(self.sol.makeGood(""), "")

    def test_non_matching_case(self):
        # Should not remove because cases are the same
        self.assertEqual(self.sol.makeGood("a"), "a")
        self.assertEqual(self.sol.makeGood("aa"), "aa")
        self.assertEqual(self.sol.makeGood("abcABC"), "abcABC")
        
    def test_long_input(self):
        # Ensuring O(N) performance
        s = "a" * 5000 + "A" * 5000
        self.assertEqual(self.sol.makeGood(s), "")

if __name__ == '__main__':
    unittest.main()

# Follow up 2: How will I solve it without using stack and give me a dry test run?
# Without using a stack, we could use a two-pointer approach to simulate the cancellation process.
# We would iterate through the string and use two pointers to identify adjacent characters that are the same letter in different cases.
# When such a pair is found, we remove it and continue processing the remaining string.
# This approach would be less efficient than using a stack but still valid.
def makeGoodWithoutStack(s: str) -> str:
    i = 0
    while i < len(s) - 1:
        if abs(ord(s[i]) - ord(s[i + 1])) == 32:
            s = s[:i] + s[i + 2:]  # Remove the bad pair
            i = max(i - 1, 0)  # Move back to check for new pairs
        else:
            i += 1
    return s
# Dry run:
# Input: "leEeetcode"
# i=0: 'l' and 'e' are not a bad pair, move to i=1
# i=1: 'e' and 'E' are a bad pair, remove them -> s = "leetcode", move back to i=0
# i=0: 'l' and 'e' are not a bad pair, move to i=1
# i=1: 'e' and 'e' are not a bad pair, move to i=2
# i=2: 'e' and 't' are not a bad pair, move to i=3
# i=3: 't' and 'c' are not a bad pair, move to i=4
# i=4: 'c' and 'o' are not a bad pair, move to i=5
# i=5: 'o' and 'd' are not a bad pair, move to i=6
# i=6: 'd' and 'e' are not a bad pair, move to i=7
# i=7: 'e' and 'e' are not a bad pair, move to i=8
# End of string reached, return "leetcode"
