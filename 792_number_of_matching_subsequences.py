class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        '''         
        abcde       The bottleneck with brute force approach is, for every word,
        a....       it goes through the given string S, which is max 5000 char
        .bb..       length, making time complexity O(N*M) where
        a.cd.       m is the num of words, n is the max len.
        a.c.e       
        
        Time: O(n+m*l) m=total number of words, l=average length of the word
        Space: O(m*l) in the worst case, word can be lengthy and only last char not matching.
        '''
        # Part 1. Dictionary to store words grouped by their first character
        # Key: character, Value: deque of words starting with that character
        waiting_dict = defaultdict(deque)

        # Group all words by their first character
        for word in words:
            waiting_dict[word[0]].append(word)
            # it will create dict={ "a":[a, acd, aec], "b":[bb] }

        # Part 2. Counter for words that are subsequences of s
        match_count = 0

        # Process each character in string s
        for char in s:
            # Process all words currently waiting for this character
            # Use len() to get current queue size to avoid infinite loop
            current_queue_size = len(waiting_dict[char])
            
            # processes only "a":[a,acd,aec] at once
            for _ in range(current_queue_size):
                # Get the word from front of queue
                current_word = waiting_dict[char].popleft()
                # first "a", second "acd", then "aec" will be popped
                # BUT POP is happening only when char == "a":[a, acd, aec]

                # If this was the last character needed, word is a subsequence
                if len(current_word) == 1:
                    match_count += 1
                else:
                    # Move word to queue for its next required character
                    # Remove first character and add to appropriate queue
                    next_char = current_word[1]
                    remaining_word = current_word[1:]
                    waiting_dict[next_char].append(remaining_word) # "c":[cd], "e":[ec]

        return match_count
        # the leftover items in the waiting_dict = {e:[c], b:[b]}, counter=2 with ["a", "acd"]