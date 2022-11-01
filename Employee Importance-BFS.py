#BFS
#Time Complexity:: O(n*s)-all nodes are visited in each level and Null values are also process
#Space Complexity:: O(n*s)-a list is used at each level, in this case usually less than O(n) as each level has a root element not included in list

"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        adj = {emp.id: emp for emp in employees} #creating adjacency matrix

        q = deque([id]) #creating q to store id of employees subs
        Result = 0 #adding importance
        
        while q:
            emp_id = q.popleft() #pop the employee id
            Result += adj[emp_id].importance #add the employee importance
            
            for subordinates in adj[emp_id].subordinates: #add the subordinates into the q to find their importance
                q.append(subordinates)
        return Result #returning given ID's importance
        