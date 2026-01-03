class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic stack, Time: O(n), Space: O(m) 
        # worst scenario is 1*m [4,3,2,1], 
        # best scenario m length array [1,2,3,4]
        wait_time = [0] * len(temperatures) # if there is no warmer day coming, by default they should be 0

        colder_days = [] # stack to store only colder days than current
        colder_days.append((0, temperatures[0])) # day number and temperature of the first element

        for curr_day, curr_temp in enumerate(temperatures):
            
            while colder_days and curr_temp > colder_days[-1][1]: # compare with the latest temp
                
                prev_day, prev_temp = colder_days.pop()
                wait_time[prev_day] = curr_day - prev_day

            colder_days.append((curr_day, curr_temp)) # runs everytime
        
        return wait_time

        """ Example 1: temperatures = [73,74,75,71,69,72,76,73]    wait_time = [0,0,0,0,0,0,0,0]
            curr_day, curr_temp = [0,73]    colder_days = [(0,73)]
            curr_day, curr_temp = [1,74]    we found warmer temp, we want to update wait_time[0], wait_time=[1-0,0,0,0,0,0,0,0]
            curr_day, curr_temp = [2,75]    colder_days = [(1,74)]
                                            we found warmer temp, we want to update wait_time[1]=2-1, wait_time=[1,1,0,0,0,0,0,0]
            curr_day, curr_temp = [3,71]    when we find colder temp, we store it, so later we can traverse backwards and
                                            calculate the distance between the warmer day and these cold days.
                                            colder_days = [(2,75) (3,71)]
            curr_day, curr_temp = [4,69]    colder_days = [(2,75) (3,71) (4,69)]
            curr_day, curr_temp = [5,72]    we found warmer temp than last(69), we want to update this for wait_time[4]=5-4
                                            wait_time = [1,1,0,0,1,0,0,0]
                                            colder_days = [(2,75) (3,71)]
                                            in while loop, we check if curr is warmer than 3rd day temp 71, it is. we want to
                                            update wait_time[3]=5-3
                                            wait_time = [1,1,0,2,1,0,0,0]
            curr_day, curr_temp = [6,76]    colder_days = [(2,75) (5,72)]
                                            we found warmer temp, we want to update wait_time[5]=6-5
                                            wait_time = [1,1,0,2,1,1,0,0]
                                            in while loop, we check if curr is warmer than 2nd day temp 75, it is. we want to   
                                            update wait_time[2]=6-2
                                            wait_time = [1,1,4,2,1,1,0,0]
            curr_day, curr_temp = [7,73]    colder_days = [(7,73)] there are no more days to iterate, the default value is
                                            already set for day 7 as wait_time[7]=0

            Example 2: temperatures = [30, 40, 50, 60]     colder_days = [(0,30)]    wait_time = [0, 0, 0, 0]
            cur_day, cur_temp = (1,40)  we found warmer temp, we want to update wait_time[0]=1-0
            cur_day, cur_temp = (2,50)  we found warmer temp, we want to update wait_time[1]=2-1
            cur_day, cur_temp = (3,60)  we found warmer temp, we want to update wait_time[2]=3-2 => wait_time=[1,1,1,0]
        """

        # Brute force
        # Time complexity: O(n^2)
        # Time limit exceeded
        # wait_time = [0] * len(nums)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] < nums[j]:
        #             wait_time[i]=j-i
        #             break
        # return wait_time