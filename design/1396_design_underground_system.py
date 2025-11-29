class UndergroundSystem:

    def __init__(self):
        # to calculate the checkout, we need to store the incomplete journeys
        self.activeJourney = {}
        # to calculate the avg time, we need a map calc between start and final stations
        # in format similar to (srcStation, destStation):(total_count, timeDiff)
        self.routeMap = {}

    def checkIn(self, userid: int, stationName: str, t: int) -> None:
        # time: O(n)
        # for every user id, we need to store its starting station with starting time
        self.activeJourney[userid]=(stationName, t)

    def checkOut(self, userid: int, destStation: str, endTime: int) -> None:
        # time: O(1) for hashmap key check then update
        # when the given user leaves the train, register route avg time
        # query when the user onboarded, where did the travel start
        srcStation, startTime = self.activeJourney[userid]

        currentRoute = (srcStation, destStation)
        if currentRoute in self.routeMap:
            # if the route has been traveled already (must be diff user),
            # then update route info for later average time calculation
            totalsum, totalnum = self.routeMap[currentRoute] # returns tuple
            self.routeMap[currentRoute] = (totalsum+endTime-startTime, totalnum+1)
        else:
            # this route needs to be registered.
            self.routeMap[currentRoute] = (endTime-startTime, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # time: O(1)
        # the average time for users to travel between 2 stations will be the avg of
        # total time spent / total number of stations in between
        totalsum, totalnum = self.routeMap[(startStation, endStation)]

        return totalsum / totalnum


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)