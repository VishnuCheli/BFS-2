#Time Complexity:: O(m*n)-all nodes are visited in the matrix
#Space Complexity:: O(n)-size of q and all operations are done inplace/ 
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        m=len(mat) #no. of rows
        n=len(mat[0]) #no. of columns
        dirs = [[0,1],[1,0],[0,-1],[-1,0]] #creating a four directional array
        q = deque() #creating a queue
        
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0: #if cell is 0 then add it to the q
                    q.append((i,j))
                else: #if cell is 1 then make it -1
                    mat[i][j] = -1
        dist = 0 #initially distance is 0
        while q:
            size = len(q)
            dist += 1 #increment the distance every time you're about to pop from q
            for num in range(size): 
                curr = q.popleft() #the current cell is initiated
                for x,y in dirs: #check all directions of the current cell
                    nr = x + curr[0]
                    nc = y + curr[1]
                    #boundary checks
                    if nr>=0 and nr<m and nc>=0 and nc<n and mat[nr][nc]==-1: #if all boundary conditions pass and -1(aka 1) is present in the neighbouring cells
                        mat[nr][nc] = dist #change the value of the cell to current distance
                        q.append((nr,nc)) #add the modified cell to the queue to check for it's neighbours
                        
        return mat #return the final result