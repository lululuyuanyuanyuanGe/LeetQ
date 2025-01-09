class Solution:
    def intToRoman(self, num: int) -> str:
        roman_rep = ''
        roman_to_dec = [
            (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
            (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'),
            (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
        ]
        for i in range(len(roman_to_dec)):
            letter_count = num // roman_to_dec[i][0]
            roman_rep += roman_to_dec[i][1] * letter_count
            num -= letter_count * roman_to_dec[i][0]
        return roman_rep