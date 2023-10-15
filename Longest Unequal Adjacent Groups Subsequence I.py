class Solution:
    def getWordsInLongestSubsequence(self, n: int, words: List[str], groups: List[int]) -> List[str]:

        subsequence = []
        last_group = None

        for i in range(n):
            if groups[i] != last_group:
                subsequence.append(words[i])
                last_group = groups[i]

        return subsequence
      
#Himel Sarder
#Dept. of CSE, BSFMSTU
  
