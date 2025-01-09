class Solution:
    def reverseWords(self, s: str) -> str:
        sentence = s.split()
        reversed_sentence = sentence[::-1]
        return ' '.join(reversed_sentence)
