class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:

        rows,cols=len(dungeon),len(dungeon[0])

        dp=[[float("inf")]*cols for _ in range(rows)]

        def getMinimumHealth(currCell,nextRow,nextCol):
            if nextRow>=rows or nextCol>=cols:
                return float("inf")
            
            nextCell=dp[nextRow][nextCol]

            return max(1,nextCell-currCell)

        for row in reversed(range(rows)):
            for col in reversed(range(cols)):

                currCell=dungeon[row][col]

                rightHealth=getMinimumHealth(currCell,row,col+1)
                downHealth=getMinimumHealth(currCell,row+1,col)

                nextHealth=min(rightHealth,downHealth)

                if nextHealth != float('inf'):
                    minHealth=nextHealth
                else:
                    minHealth=1 if currCell>0 else 1-currCell
                dp[row][col]=minHealth

        return dp[0][0]
