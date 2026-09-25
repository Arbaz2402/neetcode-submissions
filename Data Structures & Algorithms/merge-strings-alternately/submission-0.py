class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        a = 0
        b = 0
        final = ""
        while a<len(word1) and b<len(word2):
            final += word1[a]
            final+= word2[b]
            a+=1
            b+=1
        
        if a<len(word1):
            final = final + word1[a:]

        
        if b<len(word2):
            final = final + word2[b:]
        return final