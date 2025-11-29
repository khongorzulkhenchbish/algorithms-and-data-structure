class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        """ Solution 2. Two pass, O(n) time, O(n) space, without stack
        """ 
        valid1 = []
        balance = 0
        
        #  removes the extra )s that doesn't have ( before it
        for char in s:
            if char == "(":
                valid1.append(char)
                balance += 1
            elif char == ")" and balance > 0:
                # only if ) has ( before it
                valid1.append(char)
                balance -= 1
            elif char.isalpha(): # O(1) time
                # is letter
                valid1.append(char)
        
        # do the same, just in reverse order
        # so we can eliminate the ( that doesn't have ) after them
        balance = 0
        valid1.reverse() # in-place
        valid2 = []
        for char in valid1:
            if char == ")":
                valid2.append(char)
                balance += 1
            elif char == "(" and balance > 0:
                # only if ( has ) after it
                valid2.append(char)
                balance -= 1
            elif char.isalpha():
                # is letter
                valid2.append(char)
        
        # revert back
        valid2.reverse()
        return ''.join(valid2)

        """ Solution 1. O(n~) time, O(n) space, with stack
        last = []
        last_ind = []
        answer = ""
        
        i = 0
        while i < len(s): # 3 cases
            # 1. normal letter
            if s[i].isalpha():
                pass
            # 2. opening (
            elif s[i] == "(":
                last.append(s[i])
                last_ind.append(i)
            # 3. closing )
            else:
                if last and last[-1] == "(":
                    last.pop()
                    last_ind.pop()
                else:
                    last.append(s[i])
                    last_ind.append(i)
            i += 1
        
        # check if we need to remove anything
        for k in range(len(s)):
            if k not in last_ind:
                answer += s[k]
            k += 1
        
        return answer
        """