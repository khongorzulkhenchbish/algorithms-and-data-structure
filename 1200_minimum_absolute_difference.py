class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        # Time: O(N*LogN), Space: O(N)
        arr.sort()
        mindiff = float('INF')
        ans = []

        for i in range(len(arr)-1):
            diff = arr[i+1]-arr[i]
            if diff < mindiff:
                mindiff = diff
                ans = []
                ans.append([arr[i], arr[i+1]])
            elif diff == mindiff:
                ans.append([arr[i], arr[i+1]])
            else:
                pass
        
        return ans
