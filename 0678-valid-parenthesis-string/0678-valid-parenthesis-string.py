class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min = left_max = 0 # possible counts of (

        for char in s:
            if char == '(':
                left_min += 1
                left_max += 1
            elif char == ')':
                left_min -= 1
                left_max -= 1
            else:
                left_min -= 1
                left_max += 1
            
            if left_max < 0: # ) comes before ( so invalid
                return False
            if left_min < 0: # s = ( * ) (
                left_min = 0
        
        return left_min == 0 # if all ( get closed, string is valid
