from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result = defaultdict(list)  # Create a defaultdict with list as the default value type

        # Iterate over each string in the input list
        for string in strs:
            sorted_string = ''.join(sorted(string))  # Sort the characters of the string
            result[sorted_string].append(string)  # Use the sorted string as the key in the dictionary

        # Convert the result dictionary values to a list and return it
        return list(result.values())
    
#time: O(n*mlogm)
#space: O(n*m)

strs = ["eat","tea","tan","ate","nat","bat"]
solution_instance = Solution()
print(solution_instance.groupAnagrams(strs))