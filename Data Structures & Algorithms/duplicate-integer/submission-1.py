class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset=set()
        for elem in nums:
            if elem not in hashset:
                hashset.add(elem)
            else:
                return True
        return False
   