class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #Initialize set with array content and counter
        numSet = set(nums)
        longest = 0

        for n in nums:
            # for every number, if the left neighbor is in our set, initialize a local counter
            if (n - 1) not in numSet:
                length = 0
                # while n + the current length is in the set, increase the local length, it will stop when there is no right neighbor
                while (n + length) in numSet:
                    length += 1
                #If the local counter is larger than the global, replace, else stay
                longest = max(length, longest)
        return longest
