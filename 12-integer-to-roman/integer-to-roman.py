class Solution:
    def intToRoman(self, num: int) -> str:
        roman_rep = ''
        roman_to_dec = [(1, 'I'),
                        (4, 'IV'),
                        (5, 'V'),
                        (9, 'IX'),
                        (10, 'X'),
                        (40, 'XL'),
                        (50, 'L'),
                        (90, 'XC'),
                        (100, 'C'),
                        (400, 'CD'),
                        (500, 'D'),
                        (900, 'CM'),
                        (1000, 'M')]
        roman_to_dec.sort(reverse=True)
        for i in range(len(roman_to_dec)):
            letter_count = num // roman_to_dec[i][0]
            roman_rep += roman_to_dec[i][1] * letter_count
            num -= letter_count * roman_to_dec[i][0]
        return roman_rep