from collections import defaultdict
from bisect import bisect_right

class TimeMap:

    def __init__(self):
        # Using defaultdict(list) avoids the 'if key in self.keyval' check
        self.keyval = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # O(1) - Just appending to the list
        self.keyval[key].append((timestamp, value))


    def get(self, key: str, timestamp: int) -> str:
        # ["TimeMap","set","set","get" ...]
        # [[],["a","bar",1],["x","b",3],["b",3] ...]
        if key not in self.keyval:
            return ""

        # O(N) => When you have sorted data and you need to find a value,
        # the "Google Answer" is almost always Binary Search.
        # O(log N) - Binary Search

        values = self.keyval[key]

        # We search for the timestamp in our list of (timestamp, value) tuples
        # bisect_right finds the insertion point to the right of the target
        idx = bisect_right(values, (timestamp, chr(127)))
        
        # if idx is 0, it means all timestamps are greater than the target
        # ["TimeMap","set","set","get" ...]
        # [[],["love","high",10],["love","low",20],["love",5] ...]
        # no such value below 5 with key "love"
        if idx == 0:
            return ""
        
        # The correct value is at index idx - 1
        return values[idx - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)