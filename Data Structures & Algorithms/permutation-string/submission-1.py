class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False

        count1 = {}
        window = {}

        # Frequency of s1
        for char in s1:
            count1[char] = count1.get(char, 0) + 1

        l = 0

        for r in range(len(s2)):

            # Add current character
            window[s2[r]] = window.get(s2[r], 0) + 1

            # Keep window size <= len(s1)
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1

                if window[s2[l]] == 0:
                    del window[s2[l]]

                l += 1

            # Check when window size equals len(s1)
            if r - l + 1 == len(s1):
                if window == count1:
                    return True

        return False



