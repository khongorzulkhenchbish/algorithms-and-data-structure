## BlIND 75
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


## BLIND 150
| Problem Name | Solution |
|---------|---------|
| a       | b       |