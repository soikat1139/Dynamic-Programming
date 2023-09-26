class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #Dynamic Programming Solution .I kinda Like This Solution Though This is really A good Solution

        #Here we start Our Programming :

        # The approach is first of all to check all the coloumns of the first row which is basically like grid[0][cols]
        # then checking all the rows of first col like grid[rows][0]

        # If I find any obstacle then I need to mark them as zero

        # Then the solution pretty much become like unique Path 1 problem 
        # So Let's dive into the problem  Let's do this yayay

        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])

        if obstacleGrid[0][0]==1:
            return 0

        obstacleGrid[0][0]=1

        for i in range(1,cols):
            obstacleGrid[0][i]=int(obstacleGrid[0][i]==0 and obstacleGrid[0][i-1]==1)

        for j in range(1,rows):
            obstacleGrid[j][0]=int(obstacleGrid[j][0]==0 and obstacleGrid[j-1][0]==1)

        for row in range(1,rows):
            for col in range(1,cols):
                if obstacleGrid[row][col]==0:
                    obstacleGrid[row][col]=obstacleGrid[row-1][col]+obstacleGrid[row][col-1]
                else:
                    obstacleGrid[row][col]=0
        
        return obstacleGrid[rows-1][cols-1]
