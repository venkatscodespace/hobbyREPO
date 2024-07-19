class Solution(object):
    def findPeakElement(self, nums):
        if 1 <= len(nums) <= 1000:
            nums.append(None)
            l=[nums[i] for i in range(len(nums)) if -2**31 <= nums[i] <= 2**31 - 1 and nums[i] != nums[i + 1]]
            return l.index(max(l))
