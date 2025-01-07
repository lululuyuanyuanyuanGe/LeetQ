class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        start = 0
        str_ind = {}
        
        for end in range(len(s)):
            if s[end] in str_ind and str_ind[s[end]] >= start:
                start = str_ind[s[end]] + 1

            str_ind[s[end]] = end

            max_len = max(max_len, end - start + 1)
        
        return max_len