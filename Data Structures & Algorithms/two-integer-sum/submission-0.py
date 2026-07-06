class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for i, item in enumerate(nums):
            complement=target-item
            if complement in hashmap:
                return [hashmap[complement],i]
            hashmap[item]=i