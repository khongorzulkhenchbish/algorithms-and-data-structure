class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        Time: O(N+M), Space: O(N)
        case 1: overlap
        [0,2]
        [1,5] => [max(0,1), min(2,5)] => [1,2] => end1 > end2 => j+1, if end1 < end2, i+1

        case 3: no overlap
        [1,2]
        [3,5] => end1 < start2 (i+1) or end2 < start1 (j+1) no overlap
        """
        i = j = 0
        l1 = len(firstList)
        l2 = len(secondList)
        overlaps = []

        while i < l1 and j < l2:
            start1, end1 = firstList[i][0], firstList[i][1]
            start2, end2 = secondList[j][0], secondList[j][1]

            # no overlap
            # |---|
            #         |----|
            if end1 < start2:
                i += 1
            #         |----|
            # |---|
            elif end2 < start1:
                j += 1
            else:
                # overlap
                start, end = max(start1, start2), min(end1, end2)
                overlaps.append([start, end])

                # |-------|
                # |---| next -> |---|
                if end1 > end2:
                    j += 1
                #   |----|          |----|
                # |------| then any |----|
                # or
                # |---| next -> |-----|
                # |------|  |-----|    
                else: # end1 <= end2:
                    i += 1
            
            # print([start1,end1], [start2,end2], [overlaps[-1][0],overlaps[-1][1]])
        return overlaps
        # first = [[3,10],[14,15]], 
        # second = [[5,10],[13,16]]
        # output = [[3,10],[14,15]] 



