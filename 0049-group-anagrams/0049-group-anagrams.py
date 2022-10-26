class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for str in strs:
            anagrams[''.join(sorted(str))].append(str)
        
        return list(anagrams.values())