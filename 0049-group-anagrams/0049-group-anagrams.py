class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_to_words = dict()
        
        for s in strs:
            key = "".join(sorted(s))
            if key not in anagram_to_words:
                anagram_to_words[key] = []
            anagram_to_words[key].append(s)
        
        ans = []
        for words in anagram_to_words.values():
            ans.append(words)
        return ans
                