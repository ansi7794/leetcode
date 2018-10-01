class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen = {}
        maxsub = 0
        start = 0
        for end in range(len(s)):
            if s[end] in seen:
                start = max(start, seen[s[end]]+1)
            seen[s[end]] = end
            maxsub = max(maxsub, end-start+1)
        return maxsub

if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstring("abcabcbb") == 3)
    print(Solution().lengthOfLongestSubstring("abba") == 2)
    print(Solution().lengthOfLongestSubstring("pwwkew") == 3)
