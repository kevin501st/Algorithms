class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        min_length = 10 ** 50
        flag = False
        running_sum = 0
        count = 0
        left = 0
        i = 0
        while i < len(nums):
            running_sum += nums[i]
            count += 1
            i += 1
            while running_sum >= s:
                if count <= min_length and running_sum >= s:
                    min_length = count
                    flag = True
                running_sum = 0
                count = 0
                left = left + 1 if left <= (len(nums) - 1) else left
                i = left

        return min_length if flag else 0

a = Solution()
print(a.minSubArrayLen(4, [1,4,4]))