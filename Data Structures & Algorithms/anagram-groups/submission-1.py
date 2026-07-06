class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap={}
        for elem in strs:
            count=[0]*26
            for c in elem:
                count[ord(c)-ord('a')]+=1
            key=tuple(count)
            if key not in hashmap:
                hashmap[key]=[]
            
            hashmap[key].append(elem)
        return list(hashmap.values())

     