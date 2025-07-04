class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashmap_nums = {}
        for i in nums:
            if i not in hashmap_nums:
                hashmap_nums[i] = 1
            else:
                hashmap_nums[i] += 1

        for i in hashmap_nums:
            if hashmap_nums[i] == 1:
                return i 