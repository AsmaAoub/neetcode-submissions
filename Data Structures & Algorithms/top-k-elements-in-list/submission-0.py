class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for elem in nums:
            if elem not in freq:
                freq[elem]=1
            else:
                freq[elem]+=1
        array=sorted(freq,key=freq.get,reverse=True)
        return array[:k]
