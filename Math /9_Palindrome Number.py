class Solution:
    def isPalindrome(self, x: int) -> bool:
        original_number = abs(x)
        reverse_number = 0

        while original_number > 0 :
            last_digit = original_number % 10
            reverse_number = reverse_number * 10 + last_digit
            original_number = original_number // 10

        # check if number is palindrome
        if reverse_number == x : 
            return True
        else:
            return False
        
