#https://leetcode.com/problems/course-schedule/

from collections import defaultdict
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        dic = defaultdict(list)

        for course, prereq in prerequisites:
            dic[course].append(prereq)

        visitSet = set()

        def dfs(crs):
            if crs in visitSet:
                return False
            if dic[crs] == []:
                return True
            
            visitSet.add(crs)

            for pre in dic[crs]:
                if not dfs(pre):
                    return False
            visitSet.remove(crs)
            dic[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
