import time
from collections import defaultdict

class Twitter:

    def __init__(self):
        # Overall space: O(U + T)
        self.follows = defaultdict(set) # space: O(F) where F is follows
        self.tweets = defaultdict(list) # space: O(T) where T is total tweets
        self.timer = 0 # Simple counter is better than time.time() for consistency

    def postTweet(self, userId: int, tweetId: int) -> None:
        # time: O(1)
        self.tweets[userId].append((self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        min_heap = []
        
        # Combine user and followees
        target_users = self.follows[userId] | {userId}

        # time: O(F * K log K)
        # outer loop: we iterate F followers
        for user in target_users:
            if user in self.tweets:
                # time: K log K, where constant number K=10
                # We only need the last 10 tweets from each user
                for t_time, t_id in self.tweets[user][-10:]:
                    # time: O(log K) for each heap push
                    # it is usually O(10*log10) which is constant, therefore it depend hugely on F 
                    heapq.heappush(min_heap, (t_time, t_id))
                    # If we have 11, remove the OLDER one (the smallest timestamp)
                    if len(min_heap) > 10:
                        heapq.heappop(min_heap)

        # Sort what's left in the heap (only 10 items)
        res = []
        while min_heap:
            res.append(heapq.heappop(min_heap)[1])
        return res[::-1] # Reverse to get most recent first

    def follow(self, followerId: int, followeeId: int) -> None:
        # time: O(1)
        # user can't follow themselves
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # time: O(1), Removing/Discarding from hashset
        # discard is safer than remove, if the user is not followed at all, then it ignores
        self.follows[followerId].discard(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)