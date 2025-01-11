class Solution:
    def isValid(self, s: str) -> bool:
        track = []

        for p in s:
            if p in '([{':
                track.append(p)
            else:
                if not track:
                    return False
                last = track.pop()
                if not (p == ')' and last == '(' or p == ']' and last == '[' or p == '}' and last == '{'):
                    return False
        return not track