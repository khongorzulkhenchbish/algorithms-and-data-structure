class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """ How do you check if one string is permutation of another string?
        Approach 1: sort both and check if the sorted is equal.
        Approach 2: add the first string in set, and iterate the second string, 
                    remove values that are similar. In the end, if I have empty set => permutation
        Time: O(N), Space: O(1)
        """
        n1 = len(s1)
        n2 = len(s2)

        if n1 > n2: # n1 can't be sustring of n2
            return False
        
        count1 = [0] * 26 # creates a list of 26 zeros
        count2 = [0] * 26
        
        # build up the freq list, the ASCII-97 will be the index
        for i in range(n1):
            count1[ord(s1[i])-97] += 1
            count2[ord(s2[i])-97] += 1

        if count1 == count2: # we've found the substring already
            return True

        for i in range(n1, n2):
            count2[ord(s2[i])-97] += 1  # count the freq for s2
            count2[ord(s2[i-n1])-ord('a')] -= 1 # we lose the char to maintain same length

            if count1 == count2:
                return True
        
        return False
        """ Example
        s1 = "adc", s2 = "dcda"
        count1 = [1,0,1,1,.]   count2 = [0,0,1,2]
        i=3 => s2[i]=a => count2 = [1,0,1,2] # add
        ord(s2[0]) => ord(d) => 100-97 => 3 => count2 = [1,0,1,1,.] equal to a
        """
