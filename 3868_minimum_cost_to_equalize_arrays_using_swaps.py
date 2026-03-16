from collections import Counter

class Solution:
    def minCost(self, nums1: list[int], nums2: list[int]) -> int:
        # Step 1: Count total frequencies across both arrays
        # O(n) time, O(n) space
        total_counts = Counter(nums1) + Counter(nums2)

        # Step 2: Determine target state (each array gets half)
        # and check if equalization is even possible
        target_map = {}
        for num, count in total_counts.items():
            if count % 2 != 0:
                return -1 # eliminate, early on if elem is odd times appearing
            else:
                target_map[num] = count // 2


        # Step 3: Count how many elements in nums1 need to be swapped out
        # We only care about the 'excess'
        map1 = Counter(nums1)

        swap_needed = 0
        for num, count in map1.items():
            if count > target_map[num]:
                swap_needed += (count - target_map[num])
        
        # Because the arrays are the same length and total counts are even,
        # every element we swap OUT of nums1 is guaranteed to be replaced
        # by an element we actually NEED from nums2.
        return swap_needed