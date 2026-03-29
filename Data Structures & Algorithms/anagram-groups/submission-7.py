from collections import Counter 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        used_indexes = set()
        
        for i, word1 in enumerate(strs):
            if i in used_indexes:
                continue

            current_word_anagrams = [word1]
            used_indexes.add(i)

            for j, word2 in enumerate(strs):
                if i == j or j in used_indexes:
                    continue

                if Counter(word1) == Counter(word2):
                    current_word_anagrams.append(word2)
                    used_indexes.add(j)
            
            result.append(current_word_anagrams)
            
        
        return result