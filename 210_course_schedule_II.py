from collections import deque, defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # This problem is equivalent to finding the topological order in a directed graph.
        # If a cycle exists, no topological ordering exists and therefore it will be
        # impossible to take all courses.

        # Kahns algorithm(BFS): repeatedly remove vertices with no dependencies from the graph
        # and add them to the topological ordering. We do the same step until all nodes are
        # visited or the cycle is detected.

        # Time Complexity: O(V + E) where V is the number of courses and E is the number of prerequisites.
        # Space Complexity: O(V + E) for the adjacency list and in-degree array.
        
        # 1. Build Adjacency List and In-Degree Array
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            in_degree[course] += 1
            
        # 2. Initialize Queue with courses that have 0 prerequisites
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        
        result = []
        
        # 3. Process the queue
        while queue:
            current_course = queue.popleft()
            result.append(current_course)
            
            # Reduce the in-degree of all dependent courses
            for neighbor in adj[current_course]:
                in_degree[neighbor] -= 1
                
                # If a course has no more dependencies, it's ready to be taken
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # 4. If we couldn't take all courses, there's a cycle
        if len(result) == numCourses:
            return result
        else:
            return []