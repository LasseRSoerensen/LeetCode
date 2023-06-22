#https://leetcode.com/problems/group-anagrams/
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        temp_results = {}

        for i in strs: 
            if self.Sorting(i) in temp_results:
                temp_results[self.Sorting(i)].append(i)
            else: 
                temp_results[self.Sorting(i)] = [i]
        return [x for x in temp_results.values()]
    
    def Sorting(self, inp): 
        inp = ''.join(sorted(inp, key=str.lower))
        return inp



input = ["bat", "tab", "kak", "sap", "psa"]

run = Solution()
print(run.groupAnagrams((input)))


