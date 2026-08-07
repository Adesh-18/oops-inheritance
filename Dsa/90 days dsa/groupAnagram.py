from collections import defaultdict

class Solution:
    def __init__(self):
        self.strs = ["eat","tea","tan","ate","nat","bat"]
    
    def groupAnagrams(self):
        groups = defaultdict(list)
        
        for word in self.strs:
            key = ''.join(sorted(word))   # sorted word as key
            groups[key].append(word)
        
        return list(groups.values())


# run
obj = Solution()
print(obj.groupAnagrams())