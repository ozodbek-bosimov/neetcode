# # Bbute-force
# from collections import deque

# # T: O(n^2)
# # S: O(n)
# class Solution:
#     def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
#         students = deque(students)
#         sandwiches = deque(sandwiches)
#         last_len = len(students) + 1
#         while students and last_len != len(students):
#             last_len = len(students)
#             for _ in range(last_len):
#                 if students[0] == sandwiches[0]:
#                     students.popleft()
#                     sandwiches.popleft()
#                 else: students.append(students.popleft())

#         return len(students)


# T: O(n)
# S: O(1)
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        like_c = like_s = 0
        for student in students:
            if student == 1: like_s += 1
            else: like_c += 1
        
        for sandwich in sandwiches:
            if sandwich == 1:
                if like_s > 0: like_s -= 1
                else: break
            else:
                if like_c > 0: like_c -= 1
                else: break
        return like_c + like_s
