class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        phone = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        result = []
        
        def backtrack(index, current):
            # Base case: built a combination for every digit
            if index == len(digits):
                result.append(current)
                return
            
            possible_letters = phone[digits[index]]
            for letter in possible_letters:
                backtrack(index + 1, current + letter)
        
        backtrack(0, "")
        return result