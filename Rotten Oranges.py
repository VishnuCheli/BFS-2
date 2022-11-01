#Time Complexity:: O(m*n)-all cells are visited once
#Space Complexity:: O(m*n)-each element in the grid has rotten oranges
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        time = 0 
        freshcount = 0
        q = deque()
        dirs = [[1,0],[0,1],[-1,0],[0,-1]] # directions to check for each cell
        for i in range(m): #2d matrix traversal to count the number of rotten and fresh oranges
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j)) #we start from the rotten oranges so need to push into queue
                elif grid[i][j] == 1: 
                    freshcount += 1

        while q and freshcount!=0: #if all the rotten oranges and thir neighbours have been traversed, and the freshcount is 0 then exit
            time += 1 #time increases everytime we check the neighbours of a cell with a rotten orange
            size = len(q) #finding the new length of the q that holds the previous neighbours that have rotted oranges 
            
            for orange in range(size): #each new q holds the neighbours of the last popped cell that have been changed to rotten
                curr = q.popleft() #cell to move from
                for r,c in dirs:
                    nr = r + curr[0] #direction to shift the row
                    nc = c + curr[1] #direction to shift the column
                    
                    if nr>=0 and nr<m and nc>=0 and nc<n: #boundary condition
                        if grid[nr][nc] == 1: #if fresh then change to rotten since its a 4 directionally adjacent neighbour
                            grid[nr][nc] = 2 #changing fresh to rotten
                            freshcount -= 1 #fresh to rotten so update fresh count
                            q.append((nr,nc)) #passing the new co-ordinate into the q to continue checking each cell
                            
        
        if freshcount == 0: #rtype is the time count to rot every orange
            return time  #the required output
        else:
            return -1 #if there are fresh oranges after traversing all oranges to check for rottage