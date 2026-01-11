## Pattern recognition

Find the $k$-th smallest/largest element => Min-Heap / Max-Heap (Priority Queue), Quickselect (Partitioning), Trie

Priority q has O(1) insertion and deletion time.
With Heat insertion and deletion will be O(logN).
Heap is a 
1. COMPLETE binary tree, 
2. where children nodes values are always higher than the parent node value.
The max/min value of the heap can be attained on O(1) time.

Min Heap: top element has the smallest value. From top to bottom, the node values increases.
Max Heap: top element has the largest value. From top to bottom, the nodes values decreases.


#### Tree
Full binary tree: all of the nodes have either 0 or 2 offspring, excluding the leaf nodes.
Complete binary tree: the node should be filled from the left to right. if there was a skip, then it is not complete anymore.

#### 🌳 Why DFS on a binary tree uses O(height) space
When you run DFS recursively, each recursive call goes **one level deeper** into the tree. Each recursive call is placed on the **call stack**.

So the **maximum** number of stack frames at the same time equals: O(H). Let's say given tree

        A
       / \
      B   C
     / \
    D   E
         \
          F

Height of the tree: **3** if by edges.
#### 🧠 What happens to the call stack during DFS?
```python
# Steps and call stacks at that step
dfs(A):                 # 1. Call stack: [A]
    dfs(B):             # 2. Call stack: [A], [B]
        dfs(D)          # 3. Call stack: [A], [B], [D] => equal to Height 3
        dfs(E):         # 4. Call stack: [A], [B], [E] because we returned from [D]
            dfs(F)      # 5. Call stack: [A], [B], [E], [F] => depth 4, the longest root→leaf path plus 1
    dfs(C)              # 6. Call stack: [A], [B] it shrank back to 2 because we dropped [B, E, F]
    ...
```

Number of nodes = **4**\
Height (in edges) = **3**

So recursion used **O(height)** space. P.S: We know that either of them can be the space complexity. Just for overall view stating O(height) is better.

### Monotonic Stack
We can have either increasing or decreasing monotonic stack. To identify this type of problem, you should look for "find the next greater/lesser element" in the description.

**Increasing Monotonic Stack** - Find next smaller element - store those that haven't found the next smaller

```python
def nextSmallerElement(nums):
    n = len(nums)
    result = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[i] < nums[stack[-1]]:
            index = stack.pop()
            result[index] = nums[i]
        stack.append(i)
    return result
# nums =   [2,1,3,2,4, 0]
# stack =  [5]
# result = [1 0 2 0 0 -1]
```

**Decreasing Monotonic Stack** - Find next greater element - store those that haven't found the next greater
```python
def nextGreaterElement(nums):
  n = len(nums)
  result = [-1] * n
  stack = []
  for i in range(n):
    while stack and nums[i] > nums[stack[-1]]:
      index = stack.pop()
      result[index] = nums[i]
    stack.append(i)
  return result
# nums =   [2,1,3,2,4, 0]
# stack =  [4, 0]
# result = [3 3 4 4 -1 -1]
```


## BLIND 75
|Problem Name|DS & Algorithm|Difficulty|1-line solution|
|---------|---------|---------|---------|
|21. Merge Two Sorted Lists|Linked List|Easy|Imagine: changing the arrow directions, iterate both lists, move the pointers to the next if the element is merged|
|141. Linked List Cycle|Linked List, Floyd's Tortoise and Hare|Easy|Slow and Fast pointer to move ahead, check if on the same node each time|
|141. Linked List Cycle|Linked List, HashMap|Easy|Iterate, store the node if not seen, return true if node was seen|
|143. Reorder List|Linked List manipulation|Medium|Find middle point, revert the second part, later iterate both parallelly|
|19. Remove Nth Node From End of List|Linked List, two pointers|Medium|Set pointers n place apart, iterate paralllelly till the end, left.next=left.next.next|
|23. Merge k Sorted Lists|Linked List, divide and conquer|Hard|Similar approach to 21 but more optimal approach needed|
|300. Longest Increasing Subsequence|Dynamic Programming, cache|Medium|Start backwards, for every i, count the rest of j such num[i]<num[j] and cache[i]=max(cache[i], cache[j]+1)|
|53. Max Subarray|Greedy, Dynamic Programming|Medium|Kadane's algorithm, use 2 variable one for final max sum and other for every subarray sum|
|57. Insert Interval|Array, Interval|Medium|First merge smaller and separate arrays, then the rest will be always start_a <= end_b, after that do the first loop once more.|
|778. Swim in Rising Water|Binary Search, DFS|Hard|Start from the answer. Assuming the target value t' exist in range [0, n^2-1], check from the range if path exist for grid elem where cell values are less than taken t'|
|48. Rotate Image|Math, Matrix|Medium|First transpose, swap symmetric cells at each step. Then swap elements horizantally. In both of these, trick is to avoid reverting the swappes by swapping again|
|54. Spiral Matrix|Matrix, Simulation|Medium|Fix 4 corners points, left, right, top, bottom, then run iterator i,j for row,cols. update the corners after every row,col iteration|
|73. Set Matrix Zeroes|Matrix, Hash Table|Medium|Use set for first collecting the row,cols with 0s. Then later remove those r,c in the set|
|191. Number of 1 bits|Bit Manipulation|Easy|Shift the bits one by one to the right, check if the (last bit & 1), then inc counter|
|338. Counting bits|Bit Manipulation, Dynamic Programming|Easy|Find out the pattern to re-use the previous counted ones in the bit representation|
|190. Reverse Bits|Bit Manipulation|Easy|at every step in the iteration, take the right most from n then add this to the reverse, while shifting reverse to the left at every step|
|268. Missing Number|Array, Bit manipulation|Easy|diff between sum-without-missing-one and sum-with-missing-one should print missing one|

## TOP 50
|Problem Name|DS & Algorithm|Difficulty|1-line solution|
|---------|---------|---------|---------|
|215. kth largest element in the array|Heap|Medium|Use min-heap to store always at max k elements in space, the root of min-heap is the kth largest in the end. Use heapq.heappop(), heapq.heappush(), both time: O(logK)|
|680. valid palindrome II|Two pointers|Easy|Use two pointer to iterate from left and right at the same time. If there is no match use helper function to consider 2 scenarios. E.g: "abcaca" leads to removal of either b => "cac" OR c => "bca".|
|314. Binary Tree Vertical Order Traversal|BFS, Queue, Hashmap|Medium|Traverse the tree BFS, each time you go left, the column decreases, to the right, the column increases. Store the values into the hashmap {column:[vals]}. Use constant variables to store the range so you can traverse through the values in the end.|
|827. Making A Large Island|DFS, Matrix|Easy-Hard ~ 2 medium|1. Precompute the area of the islands, replace each island cells with unique label, store the areas in separate hashmap {"label":area}. 2. Flip zeros one by one, check 4 directions, increment if it connects to islands by their prestored area|
|199. binary tree right side view|Tree, BFS with deque|Medium|Traverse the tree level by level. At each level, find the rightmost val, then after the level is finished update the right view array. Use deque(), popleft()|
|408. valid word abbreviation|Two Pointer|Easy|Use two pointers to iterate at the same time. return False immediately in leading 0s or unmatching chars, for the rest just go forward. Knowing isalpha(), isdigit() is necessary!|
|1279. minimum remove to make valid parenthesis|String, Stack|Medium|Use two pass. First, accept those ")"s that appeared after "("s. In the second run, do the same, just in reversed order. Use list as string is immutable, list.reverse() does in-place reversion, "".join(list) joins list elements into string.|
|543. diameter of a binary tree|Tree, DFS|Medium|The diameter is the edge, not the vertices. At each subtree, maxdiameter is updated with sum of left and right subtrees maxd, while height is defined as max of the two then to be returned returned at end of the dfs calls.|
|347. top k frequent elements|Hashmap, Bucket Sort|Medium|Create the hashmap={"num":countNum} then convert this into arr[countNum]=[num1, num2] where the frequency will be the index and the numbers will be the list values. Notice that this bucket will have at most n elements. This is the bucket sort, return those keys/nums while iterating backwards|
|236. lowest common ancestor of a binary tree|Tree, DFS|Medium|Check every possible combination with DFS. Case 1: p and q are in separate branches => LCA node itself. Case 2: p is parent of q => p is the LCA. Case 3: q is parent of p => q is the LCA|
|235. lowest common ancestor of a binary search tree|Tree, DFS|Medium|Same as above except we check cases logn times due to the binary tree given in sorted order. Either in the left or right subtree or if it's in both, then the root itself is the LCA|
|1650. Lowest Common Ancestor of a Binary Search Tree III|Two Pointers, Binary Tree, Parent Traversal|Medium|First traverse and save the parents of p in a set. Second, traverse parents in q, if you find parent is already traversed in set, that means LCA.|
|162. Find Peak Element|Array, Binary Search|Medium|Modified binary search, you can return any of the peaks. Go left if it is increasing to the left, same logic for the right side|
|31. Next Permutation|Array, Two Pointers|Medium-Hard|Intuition: find pivot from backwards iteration that is not increasing (43|2|531), swap the pivot with num that is slightly higher than itself from the right side (43|3|521), everything else on the right side can be reverse/sorted after (43|3|125)|
|1762. Buildings With an Ocean View|Array, Monotonic stack|Medium|Instead of iterating from left to right go opposite direction. If you see a building higher than the last added one, then add that to the list. Return the reversed list indices.|
|50. Pow(x, y)|Math, Recursion|Medium|Intuition is to use binary exponentiation to optimize linear approach to logN time, consider cases 0, negative, even, odd degree of given number x|
|528. Random Pick with Weight|Binary Search, Prefix Sum, Randomized, Design|Medium|Store prefix_sums for each values and total_sum. Then when picking, get random number between [0, total_sum], use binary search to find the location of the index using the the prefix_sums list|
|339. Nested List Weight Sum|Array, DFS|Easy-Medium|Use DFS on the array, use given class functions: .getInteger(), .getList()|
|1004. Max Consecutive Ones III|Array, Sliding Window|Medium-Hard|Think of it as "What is the max subarray with k zeroes?". use sliding window, right to extend, left to shrink until we remove zero from the beginning and contain k zeroes|
|986. Interval List Intersections|Array, Sweep Line, Two Pointers|Medium|Consider no overlapping and overlapping cases. If overlapping collect the [max(start1, start2), min(end1, end2)] overlaps. Then if first end less than second start, move pointer1. Else (If second end is less than first start), move pointer2.|
|921. Minimum Add to Make Parenthesis Valid|String, Stack|Easy-Medium|If closing bracket appeared before opening one, that makes it invalid, count the num of invalids while traversing, but if the opening bracket appeared before closing one, we can eliminate that tuple out of consideration.|
|1047. Remove All Adjacent Duplicates In String|String, Stack|Easy|Iterate letters one by one, if find char that is similar to the prev, pop that from the stack. If not add in the stack. Stack will end up having unique items left.|
|78. Subsets|Array, Backtracking|Medium|NOT Permutation! At every step we should either include the number in the subset ot not include. Collect the subsets based on this cases both with dfs calls.|
|973. K Closest Points to Origin|Array, Heap|Medium|First store by [dist, x, y], then build minHeap where it will sort by te dist by default. Then pop from the smallest and return k such [x,y] points.|
|443. String Compression|Two Pointers, String|Medium|Left pointer to define writing, right pointer for iterating. Go through the elements and compare if the current char is equal to the prev one. If so, increase the counter, if not update the char with the count at write position. The count can be 2 digits, use string iteration on count to get digit by digit|
|2817. Minimum Absolute Difference Between Elements With Constraint|Binary Search, Ordered Set|Medium|For every j, process nums[0:j-x] elements, find insertion point for nums[j], then calc min diff for left and right side elements for nums[j]|
|246. Strobogrammatic Number|Hash Table, Two Pointers|Easy|Define a hash table where it contains the 180 rotated key,value pairs. Then use two pointer, iterate from both sides and check if one of the num is the rotated version of the other one|
|2043. Simple Bank System|Array, Simulation, Design, Hash Table|Easy-Medium|Check the senders balance before transfering money or depositing. Nothing special|
|173. Binary Search Tree Iterator|Stack, Tree, Design|Medium|Use stack to store the left most nodes. Pop 1-by-1, then before returning, add the right childs left most items in the stack.|
|703. Kth Largest Element in a Stream|Heap, Design|Easy|Initialize the min_heap with k elements using the add fuction. heapq.pop and heap.push both takes time: O(logN)|


## Design
|Problem Name|DS & Algorithm|Difficulty|1-line solution|
|---------|---------|---------|---------|
|1396. Design Underground System|Hashmap, Design|Medium|Use two hastables, one for storing incomplete journeys, other for aggregating the total stops between start and final stations, total time spent in those stations. The average=(totaltime/totalstops)|
|1570. Dot Product of Two Sparse Vectors|Array, Hash Table, Two Pointers|Medium|Filter nonzeros values in array [[index, value],..]. Then use two pointers to iterate at the same time and calc dot product. (Try not to use hashmap approach, on larger input it takes time to create)|
|155. Min Stack|Stack, Design|Medium|Use two stacks, keep track of the min elements alongside the original stack elements|

## OTHERS
|Problem Name|DS & Algorithm|Difficulty|1-line solution|
|---------|---------|---------|---------|
|125. valid palindrome|String, Two pointers|Easy|check the even and odd scenarios first, then filter out the non numberic and alphabetic chars, then use two pointers to start comparing from start and end, stop when start>end|
|419. battleships in a board|Array, Matrix|Medium|In each row, col there can be more than 1 ships, at each step look back upwards and to the left and count the ship if it is the first one. Edge case: board[0][0]|
|1002. find common characters|Array, Hashmap|Easy(not really)|Use 2 hashmap, one for collecting each words character frequency, another for updating after by comparing with the current word frequency. Space will not be more than 26 or O(1)|
|875. Koko Eating Bananas|Array, Binary Search|Medium|Notice that values k=[1, max(piles)]. So instead of looping over the array k times, we can do logK time by checking if the current_total_hours is less or more than the hour limit given. If we are eating slow, we should increase the speed k. Else, if we are eating fast and make it in time h, we can still try to minimize K.|
|5. Longest Palindromic Substring|Two Pointers, String|Medium|Assume every character sis possibly the middle character of palindrome, expand to both directions as much as you can. Notice that longest palindrome has either even or odd length.|
|34. Find First and Last Position of Element in Sorted Array|Array, Binary Search|Medium|If mid_val < target, target is on the right side, if mid_val > target, target is on the left side. If mid_val is equal to target then the first and last positions are in both left and right side. Therefore use a trick to call subfunction itself twice, passing a boolean value to intentionally go left and right each time.|

## BLIND 150
|Problem Name|DS & Algorithm|Difficulty|1-line solution|
|---------|---------|---------|---------|
|167. Two Sum II - Input Array Is Sorted|Array, Two Pointers|Medium|Use two pointers, if the sum is higher than target decrease the right pointer, else increase the left pointer, until the sum is found|
|42. Trapping Rain Water|Array, Two Pointers|Hard|For each cell, find it's max column to the left and right. After that, [current_water = min(left, right)-curr_height]|
|567. Permutation in String|Hash Table, Sliding Window|Medium|First form same length frequency list. Then iterate rest of the second string. At each step add the current while removing the leftmost of the sliding window from the frequency list. Use ASCII values for list indexes|
|3795. Minimum Subarray Length With Distinct Sum At Least Sum k|Array, Two Pointers, Hash Tables, Sliding Window|Medium|Use hashmap to count frequency at each step to the right. Add the subarray sums too, but just once per unique number. When find subarray with k sum, shrink from the left as much as possible.|
|239. Sliding Window Maximum|Array, Monotonic Queue, Sliding Window|Hard|TODO: Didn't understand well|
|150. Evaluate Reverse Polish Notation|Array, Stack|Medium|Using stack will make it easier because, we don't know what to do with numbers until we get the operators.|
|739. Daily Temperatures|Array, Monotonic Stack|Medium|Use monotonic decreasing stack to store colder (day, temp). If you find warmer day, update the time it took to wait "for every pairs in stack that is colder than current". If you encounter colder days, then just store it alongside temp so you can later mark the time difference when you find warmer day for them.|
