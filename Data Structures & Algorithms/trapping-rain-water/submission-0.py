class Solution:
    def trap(self, height: List[int]) -> int:

#if out of bounds, return
        if not height:
            return 0

# initialize two pointers at each corner
        l, r = 0, len(height) - 1

#Initialize storage for each maximum spot
        leftMax, rightMax = height[l], height[r]
        res = 0

#until pointers cross each other move left or right, whichever is lower
        while l < r:
            if leftMax < rightMax:
                l += 1
# change leftMax to the maximum between current pointer and previous leftMax and include that in the result
                leftMax = max(height[l], leftMax)
                res += leftMax - height[l]
            else:
# change rightMax to the maxumum between the current pointer and previous leftMax and include that in the result
                r -= 1
                rightMax = max(height[r], rightMax)
                res += rightMax - height[r]
#return Answer
        return res

    
