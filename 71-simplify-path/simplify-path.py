class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        components = path.split('/')

        for part in components:
            if part == "..":
                if stack:
                    stack.pop()
            elif part == "." or part == "" :
                continue
            else:
                stack.append(part)
        
        cononical_form = "/" + "/".join(stack)
        return cononical_form