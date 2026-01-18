class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        """ Time: O(N)    Space: O(1439)
        Use Bucket Sort to store the minutes as index. This is doing the sorting
        where the minutes are placed on that index.
        Then find diff between minutes one by one if that is recorded True.
        """
        def convert_to_min(time):
            h, m = map(int, time.split(":"))
            return int(h) * 60 + int(m)
        
        exists = [False] * (24*60)
        # to find the [00:00, ...23:59]
        first, last = 24*60, 0

        # bucket sort
        for time in timePoints:
            minute = convert_to_min(time)
            if exists[minute]: # this means the same hours exists, e.g: 12:34,12:34=0
                return 0
            # if not then mark that we found new time
            exists[minute] = True
            first = min(first, minute)
            last = max(last, minute)
        
        # find minimum difference
        min_diff = 24 * 60
        prev = first            # exists for sure
        for cur in range(prev+1, len(exists)):
            if exists[cur]:     # if this minute was noticed, calc diff
                min_diff = min(min_diff, cur-prev)
                prev = cur     # update the current
        
        # calculate to anti-clockwise direction
        min_diff = min(min_diff, 24*60+first-last)

        return min_diff
        
        """ Time: O(NlogN) Space: O(1)
        The intuition is to think of given timePoints as clock. Circular.
        Therefore the minumum minutes for ["23:59","00:00"]=1 min and ["00:00","23:59",]=1 min.
        1. We sort to avoid counting the diff as 23:59 min.
        2. We compare 2 hours at once. Hours will be sorted and it will add (last-first) edge case.
            Case 1: Both a,b are within 24 range diff=b-a
            Case 2: A is within 24, b is over 24 => b < a by minute => diff = (24*b-a)
        """
        timePoints.sort()

        for i in range(len(timePoints)-1):
            first = convert_to_min(timePoints[i])
            second = convert_to_min(timePoints[i+1])

            # [00:01, 06:00, 23:59]
            answer = min(answer, second-first)

            # optimization. If we know we found the min possible, we could stop already
            if answer == 0:
                return 0
        
        # Final step. Handling an edge case: to not miss the [23:59, 00:01]
        first = convert_to_min(timePoints[-1])
        second = convert_to_min(timePoints[0])

        if second < first:
            answer = min(answer, 24*60+second-first)
        else: # first <= second
            answer = min(answer, second-first)
        
        return answer