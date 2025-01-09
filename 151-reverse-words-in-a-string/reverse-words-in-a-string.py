class Solution:
    def reverseWords(self, s: str) -> str:
        string_list = []
        word = ''
        for i in range(len(s)):
            if s[i] is not ' ':
                word += s[i]
            else:
                if word:
                    string_list.append(word)
                    word = ''

        string_list.append(word)
        final_sentence = ''

        for i in range(len(string_list)-1, -1, -1):
            final_sentence += string_list[i]
            if i != 0:
                final_sentence += ' '
        return final_sentence.strip()
