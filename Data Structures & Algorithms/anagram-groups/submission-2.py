class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for string in strs:
            sorted_s = ''.join(sorted(string))
            result[sorted_s].append(string)
        return list(result.values())
        