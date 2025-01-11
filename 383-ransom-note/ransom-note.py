class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_letters = {}
        for l in magazine:
            if l in mag_letters:
                mag_letters[l] += 1
            else:
                mag_letters[l] = 1
        for l in ransomNote:
            if l in mag_letters:
                mag_letters[l] -= 1
                if mag_letters[l] == 0:
                    del mag_letters[l]
            else:
                return False
        
        return True
            