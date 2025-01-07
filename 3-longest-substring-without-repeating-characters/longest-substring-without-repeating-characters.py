class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        string_len = len(s)
        substring = ''

        for i in range(string_len):
            temp_substring = ''
            for j in range(i, string_len):
                if s[j] not in temp_substring:
                    temp_substring += s[j]
                else:
                    if len(temp_substring) > len(substring):
                        substring = temp_substring
                    break
            if len(temp_substring) > len(substring):
                substring = temp_substring
            if len(substring) >= string_len - i - 1:
                return len(substring)
        return len(substring)