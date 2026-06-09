# T: O(n)
# S: O(1)
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        likes = [0,0]
        for student in students:
            likes[student] += 1
        
        for sandwich in sandwiches:
            if likes[sandwich] > 0:
                likes[sandwich] -= 1
            else: break

        return sum(likes)
