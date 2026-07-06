class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     hashmap={}
     for i,elem in enumerate(nums):
        complement=target-elem
        if complement in hashmap:
            return[hashmap[complement],i]
        else:
            hashmap[elem]=i
