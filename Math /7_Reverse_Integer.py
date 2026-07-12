class Solution:
    def reverse(self, x: int) -> int:
        reverse_number = 0
        number = abs(x)

        while number > 0 :
            last_digit = number % 10
            reverse_number = reverse_number * 10 + last_digit
            number = number // 10

        # Restore the sign
        if x < 0 :
            reverse_number = -reverse_number

        # Check 32 bit signed integer range

        if reverse_number < -2**31 or reverse_number > 2**31 - 1:
            return 0

        return reverse_number
