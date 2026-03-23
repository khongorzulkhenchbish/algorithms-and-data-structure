# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Approach 2: Min Heap
        # Time: O(N log K) where N is the total number of nodes and K
        # is the number of linked lists. We are iterating through all the nodes and each time we add or remove
        # a node from the heap, it takes O(log K) time.
        # Space: O(K) because at most we will have K nodes in the heap at any time.
        if len(lists) == 0:
            return
        if len(lists) == 1:
            return lists[0]
        minHeap = []
        for i in range(len(lists)):
            if lists[i]:
                # Each list's head is pushed into the heap initially
                heapq.heappush(minHeap, (lists[i].val, i))
        
        mergedHead = merged = ListNode()
        while minHeap:
            # We repeatedly extract the smallest element
            val, idx = heapq.heappop(minHeap)
            merged.next = ListNode(val)
            #, append it to the result, 
            merged = merged.next
            if lists[idx].next:
                lists[idx] = lists[idx].next
                # and push the next element from the same list if available.
                heapq.heappush(minHeap, (lists[idx].val, idx))
        return mergedHead.next
    
        # Approach 1: Linked List Merge
        if len(lists) == 0:
            return
        if len(lists) == 1:
            return lists[0]

        prev = None
        # two or more list
        for curr in lists:
            mergedHead = merged = ListNode()
            # iterate till one of them empty
            while curr and prev:
                if prev.val <= curr.val:
                    merged.next = prev
                    prev = prev.next
                    merged = merged.next
                elif prev.val > curr.val:
                    merged.next = curr
                    curr = curr.next
                    merged = merged.next
            # if one of the list is longer
            if curr:
                merged.next = curr
            if prev:
                merged.next = prev
            
            # both should be empty at this point
            prev = mergedHead.next
        
        return mergedHead.next