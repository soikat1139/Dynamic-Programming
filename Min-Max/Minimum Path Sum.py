class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        rows,cols=len(grid),len(grid[0])

        dp=[[float("inf")]*cols for _ in range(rows)]

        def getMinimum(currCell,nextRow,nextCol):
            if nextRow>=rows or nextCol>=cols:
                return float("inf")

            nextCell=dp[nextRow][nextCol]  

            return nextCell+currCell

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):
                currCell=grid[row][col]

                rightCount=getMinimum(currCell,row,col+1)

                downCount=getMinimum(currCell,row+1,col)

                nextCount=min(rightCount,downCount)

                if nextCount != float("inf"):
                    minCount=nextCount
                else:
                    minCount=currCell
                dp[row][col]=minCount

        return dp[0][0]    
