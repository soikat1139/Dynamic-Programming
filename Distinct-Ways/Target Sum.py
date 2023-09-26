##Problem Statements for target Sum

You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and - before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1

###Problems statement In my own Own word:

So the problem is basicallly taking decision we have actually two options  we can either choose + nor - .Any problem that has decision taking section the probability of that problem being Dynamic programming is  90% except for set

Any problem that asks for actually ask  counting ways or minimum or maximum is probably dp problem:








#Brute Force Or reccursive Solution .Here It is The Reccursive Solution :I just Neeed to optimize the solution more and more So let's start:

#BRUTE FORCE SOLUTION:
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        count=0

        def calculate(idx,curr_sum):

            if idx==len(nums):
                if curr_sum==target:
                    nonlocal count
                    count+=1
            else:
                calculate(idx+1,curr_sum+nums[idx])
                calculate(idx+1,curr_sum-nums[idx])
        calculate(0,0)

        return count


#RECCURSIVE Solution with memoiziation: Here is the memoization answer for this problem : 



class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        count=0

        memo={}

        def calculate(idx,curr_sum):

            if idx==len(nums):
                if curr_sum==target:
                    return 1
                else:
                    return 0

            if (idx,curr_sum) in memo:
                return memo[(idx,curr_sum)]
                 
            
            add=calculate(idx+1,curr_sum+nums[idx])
            subtract=calculate(idx+1,curr_sum-nums[idx])

            memo[(idx,curr_sum)]=add+subtract

            return memo[(idx,curr_sum)]

        return calculate(0,0)


#### Now let's dive into the Dynamic Programming Solution :









