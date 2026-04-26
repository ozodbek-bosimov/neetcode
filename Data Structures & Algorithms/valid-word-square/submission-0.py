#  https://leetcode.com/problems/valid-word-square/
# Example 1:
# Input: words = ["abcd","bnrt","crmy","dtye"]
# Output: true
# Example 2:
# Input: words = ["abcd","bnrt","crm","dt"]
# Output: false
# Example 3:
# Input: words = ["ball", "area","lead","lady"]
# Output: true



# Time Complexity: O(n * m)
# Space Complexity: O(1)
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        words_length = len(words)
        for i in range(words_length):
            word_length = len(words[i])
            for j in range(word_length):
                if j >= words_length or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True






# if __name__ == "__main__":
#     sol = Solution()

#     words = [
#         "ball",
#         "area",
#         "lead",
#         "lady"]
    
#     # Output: true
#     print(sol.validWordSquare(words))

