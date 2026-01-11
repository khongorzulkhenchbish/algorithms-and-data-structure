class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """ The idea is that koko can eat ONLY one pile of bananas at once.
        Therefore koko can eat at most max(piles) bananas at once.
        Given a contraint finish all the bananas before "h" hours finishes,
        we have to make sure to eat at speed k that after "h" hours, we have zero left.
        Brute force approach is to check in range k=[1, max(piles)]
        [3,6,7,11] => 
        k = 1 [3,6,7,11] => total_time = 3+6+7+11 = 27 needs to eat more
        k = 2 [3,6,7,11] => total_time = 2+3+4+6 = 15 needs to eat more
        k = 3 [3,6,7,11] => total_time = 1+2+3+4 = 10 needs to eat more
        k = 4 [3,6,7,11] => total_time = 1+2+2+3 = 8 hours <= h
        k = 5 we need to find max k, so it won't make sense to continue.
        Time: k*O(N)

        Is this really optimal? - Not yet. We know that k should be between range
        [0,30] following example. Let's say eating 30 bananas at times would help,
        but running the loop over piles 30 times is not efficient.

        Therefore, using binary search to find K. If the total_hours is less than h
        with K-speed, we want to check if there are lesser k which satisfies the same
        condition in range [0,14]. Else, if the total_hours is more than h, we need
        to eat faster, so k should be in range [16,30].

        piles = [30,11,23,4,20], h = 6
        k = 15  2+2+2+1+2=9 is way higher than 6, needs to eat more, range=[16,30]
        k = 23  2+1+1+1+1=6 is same as 6 => current_mink=23, could be less still, range=[16,22]
        k = 19  2+1+2+1+2=8 is way higher than 6, needs to eat more, range=[20,22]
        k = 21  2+1+2+1+1=7 is way higher than 6, needs to eat more, range=[22,22]
        k = 22  2+1+2+1+1=7 is way higher than 6, needs to eat more, range=[23,22] => no other option
        answer => current_mink => 23

        Time: O(logk*N) Space: O(1)
        """
        k = max(piles)
        left = 1
        right = max(piles)

        while left <= right:
            mid = (left+right) // 2
            total_hours = 0
            for bananas in piles:
                total_hours += math.ceil(bananas/mid) # ceil rounds up the int. 7,2 => 4;   6,2 => 3
            if total_hours <= h:
                k = min(mid, k)
                right = mid-1
            else:
                left = mid+1
        
        return k