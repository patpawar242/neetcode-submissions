class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ana_map=defaultdict(list)
        for s in strs:
            sorted_s="".join(sorted(s))
            ana_map[sorted_s].append(s)
        return list(ana_map.values())