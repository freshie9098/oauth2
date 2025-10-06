class Solution:
    def jump(self, nums: List[int]) -> int:
        # Approach : 
        # from a given place keep expanding your frontiers. 
        # and count how many times you have to expand it = minimum number of jumps needed. 
        jumps = 0
        farthest_reach = 0
        current_reach = 0

        #Edge case : 
        if len(nums)==1:
            return 0

        for i in range(len(nums)):
            farthest_reach = max(farthest_reach,i+nums[i])
            
            if i==current_reach: 
                #update the current reach
                current_reach = farthest_reach
                jumps+=1
                if current_reach>=len(nums)-1:
                    break
        return jumps
