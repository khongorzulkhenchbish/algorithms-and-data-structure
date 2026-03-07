class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Time: O(M*N*4^L) where M and N are the dimensions of the board, and L is the length of the longest word.
        # Space: O(W*L) for the Trie, where W is the number of words and L is the average length of the words. 
        # The recursion stack can go as deep as L.
        def dfs(r, c, parent):
            char = board[r][c]
            curr_node = parent[char]

            # Step 2: Check if we found a word
            # Checks if '#' exists → returns the word value if it does, or None if it doesn't
            found_word = curr_node.pop('#', None)
            # Removes the key → after this call, '#' is no longer in curr_node
            # On a subsequent DFS path that reaches the same curr_node,
            # the '#' key is already gone, 
            # so pop returns None and the word isn't added to res "again"
            if found_word:
                res.append(found_word)

            # Step 3: Backtracking with in-place modification
            # This replaces the 'visit' set and saves O(M*N) space
            board[r][c] = "#"  # Mark as visited
            
            # we should be able to go in all directions (up, down, left, right) from the current cell
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] in curr_node:
                    # If the next character in the board exists in the current Trie node, we can continue the DFS
                    dfs(nr, nc, curr_node)
            
            board[r][c] = char  # Restore the board (backtrack)

            # Step 4: CRITICAL PRUNING
            # If the current node has no more children, it's a dead end.
            # We remove it from the parent to stop future DFS calls from entering here.
            if not curr_node:
                parent.pop(char)

        # Step 1: Build the Trie using a nested dictionary instead of a class-based TrieNode for simplicity and speed.
        # words = ["oath","pea","eat","rain"]
        # The Trie will look like:
        # root
        #  ├── 'o' ── 'a' ── 't' ── 'h' ── '# (end of "oath")
        #  ├── 'p' ── 'e' ── 'a' (end of "pea")
        #  ├── 'e' ── 'a' ── 't' (end of "eat")
        #  └── 'r' ── 'a' ── 'i' ── 'n' (end of "rain")
        root = {}
        for word in words:
            node = root # 'o', 'p', 'e', 'r'
            for char in word:
                if char not in node:
                    node[char] = {} # {} could store the children of the TrieNode
                node = node[char] # node now points to the child node for char. 'o' -> 'a' -> 't' -> 'h'
            node['#'] = word  # Mark end of word. o-a-t-h-# : "oath"

        rows, cols = len(board), len(board[0])
        res = []
        
        # Start the search
        # board = [
        # ["o",a","a","n"],
        # ["e","t","a","e"],
        # ["i","h","k","r"],
        # ["i","f","l","v"]]
        for r in range(rows):
            for c in range(cols):
                if board[r][c] in root: # searches level 1 of the Trie. 'o', 'p', 'e', 'r'
                    dfs(r, c, root) # adds the word to res if we find it

        return res