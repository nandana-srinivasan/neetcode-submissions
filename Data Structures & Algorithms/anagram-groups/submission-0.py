class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for s in strs:
            sorted_str = ''.join(sorted(s))
            seen[sorted_str].append(s)
        return list(seen.values())
            

        