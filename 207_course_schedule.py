class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Approach 2. How might switching to an iterative BFS approach with Kahn's Algorithm change
        # your space usage or handle large recursion depths?
        # Time: O(V + E), Space: O(V + E)

        # Recursion Depth: Python has a default recursion limit (usually 1,000).
        # In a graph with many nodes (like the 5,000+ constraints often seen), a DFS on a "long,
        # thin" graph (like a linked list) will trigger a RecursionError. BFS completely avoids this
        # because it uses heap memory (via the deque) rather than the call stack.

        # collect incoming degree numbers and prereq list into map
        in_degree = [0] * numCourses
        course_map = defaultdict(list)

        # "CURRENT COURSE": [courses that can be taken after current one]
        # O(E)
        for course, prev in prerequisites:
            course_map[prev].append(course)
            in_degree[course] += 1
        
        taken = 0
        # O(V)
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])

        while queue:
            course = queue.popleft()
            taken += 1

            # Reduce the in-degree of all dependent courses of CURRENT ONE
            for prev in course_map[course]:
                # as we just took current course, we have to remove it from
                # prerequisite of other courses that is demanding from current one
                in_degree[prev] -= 1

                if in_degree[prev] == 0:
                    queue.append(prev)
                
        
        if taken == numCourses:
            return True
        return False
        
        # Approach 1. Time: O(V + E)    Space: O(V + E)
        # detect the cycle in directed acyclic graph
        
        # courseReqMap = { i*[] for i in range(numCourses)}
        courseReqMap = {}
        for node in range(numCourses):
            courseReqMap[node]=[]

        # iterate through input and assign the req to the courses
        for course, req in prerequisites:
            courseReqMap[course].append(req)
        
        # along current dfs path
        visited = set()
        def dfs(currCourse):
            if currCourse in visited: # it mean we already registered the reqs of this node, cycle found!
                return False          # we can't take all the courses
            if courseReqMap[currCourse]==[]: # has no prereq, we can take this course
                return True
            
            visited.add(currCourse) # take this course
            
            # iterate through each prerequisites and check if these can be taken.
            for req in courseReqMap[currCourse]:
                if not dfs(req):    # if we find a req that forms a cycle, therefore can't be taken, 
                    return False    # then current course can't be taken as well

            courseReqMap[currCourse]=[] # this avoids duplicate dfs calls Time: O(n)
            visited.remove(currCourse)  # before exiting current path, avoid marking it as cycle

            # if the loop finishes and arrives here, that means the currCourse can be taken
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True

'''
Example 1: can be completed
numCourses = 4, prerequisites = [[0,1],[0,3],[1,3],[2,3]] there is a cycle but the courses can be taken

courseReqMap = {0: [], 1: [], 2: [], 3: []} after initializing
courseReqMap = {0: [1, 3], 1: [3], 2: [3], 3: []} "course":[list of reqs]

visited = (0, 1) => remove 1 => (0) => rmeove 0 => ()
dfs(0) => dfs(1) => dfs(3) => True, dfs(3) => True => courseReqMap = {0: [], 1: [], 2: [3], 3: []} => True

visited = () dfs(1) = True

visited = (2) => remove 2 => ()
dfs(2) => courseReqMap = {0: [], 1: [], 2: [0], 3: []} => True

visited = () dfs(3) => True

Example 2: can not be completed
numCourses = 2, prerequisites = [[1,0],[0,1]]

courseReqMap = {0:[1], 1:[0]}

visited = (0, 1)
dfs(0) => dfs(1) => dfs(0) = 0 is in the visited => False

visited = (1, 0)
dfs(1) => dfs(0) => dfs(1) = 1 is in the visited => False
'''