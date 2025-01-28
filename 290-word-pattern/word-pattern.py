class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        letter_map = {}
        word_map = {}
        words = s.split()
        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):
            l = pattern[i]
            w = words[i]
            if l in letter_map:
                if letter_map[l] != w:
                    return False
            letter_map[l] = w
            
            if w in word_map:
                if word_map[w] != l:
                    return False
            word_map[w] = l

        return True 