class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for a in asteroids:
            while a < 0 and stack and stack[-1] > 0:
                diff = stack[-1] + a
                if diff < 0:
                    stack.pop()
                    continue
                if diff == 0:
                    stack.pop()
                a = 0
                
            if a != 0:
                stack.append(a)
        
        return stack
