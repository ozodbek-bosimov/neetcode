class Solution:
    def simplifyPath(self, path: str) -> str:
        tokens = path.split("/")
        
        stack = []
        for token in tokens:
            if token  in ('', '.'):
                continue
            
            if token == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(token)

        return '/' + '/'.join(stack)
        