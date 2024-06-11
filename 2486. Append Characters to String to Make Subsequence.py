class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        s_pointer, t_pointer = 0, 0

        # Traverse through both strings
        while s_pointer < len(s) and t_pointer < len(t):
            if s[s_pointer] == t[t_pointer]:
                t_pointer += 1  # Move t_pointer if characters match
            s_pointer += 1  # Always move s_pointer

        # Return the number of characters needed to append
        return len(t) - t_pointer

#time: O(n)
#space: O(1)

s = "coaching"
t = "coding"
solution_instance = Solution()
print(solution_instance.appendCharacters(s, t))