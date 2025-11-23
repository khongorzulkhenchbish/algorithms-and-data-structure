class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # time: O(n*k) where k is length of the word.
        # space: O(1) because max length of the array will be always 26
        if len(words) == 0: return []

        # calculate the frequency of first word to initialize the common frequency map
        commonmap = {}
        for letter in words[0]:
            commonmap[letter] = 1 + commonmap.get(letter, 0)


        for word in words[1:]:
            # should be empty init for every word 
            wordmap = {}
            # count frequency of letters in current word
            for letter in word:
                wordmap[letter] = 1 + wordmap.get(letter, 0)

            # update the common frequency map after iterating each word
            for key, val in commonmap.items():
                # if the word has letters with diff number, then take the min frequency 
                commonmap[key] = min(commonmap[key], wordmap.get(key, 0))
        
        
        return [key for key, val in commonmap.items() for i in range(val) if commonmap[key] > 0]
        """
        words = ["bella","label","roller"]
        commonmap = {b:1, e:1, l:2, a:1}
        word = "label"
        wordmap = {l:2, a:1, b:1, e:1}
        commonmap updated = {b:1, e:1, l:2, a:1}
        word = "roller"
        wordmap = {r:2, o:1, l:2, e:1}
        commonmap updated = {b:0, e:1, l:2, a:0, r:0}
        return [e, l, l]
        """