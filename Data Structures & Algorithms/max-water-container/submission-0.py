class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Initialize response
        biggest = 0
        #Initialize two pointers
        l, r = 0, len(heights) - 1
        #loop until they meet
        while l < r:
            #calculate area by width * smallest wall
            currArea = (r - l) * min(heights[r], heights[l])
            # if the current area is the biggest seen, save it
            if currArea > biggest:
                biggest = currArea
            #
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        
        return biggest
        


            

