class Solution:
    def climbStairs(self, n: int) -> int:
        intermediate_climbs={1:1,2:2}
        for i in range(3,n+1):
            intermediate_climbs[i]=intermediate_climbs[i-1]+intermediate_climbs[i-2]
        return intermediate_climbs[n]

        