class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        intermediate_robber={0:nums[0],1:max(nums[0],nums[1])}
        for i in range(2,len(nums)):
            intermediate_robber[i]=max(intermediate_robber[i-1],intermediate_robber[i-2]+nums[i])
        return intermediate_robber[len(nums)-1]