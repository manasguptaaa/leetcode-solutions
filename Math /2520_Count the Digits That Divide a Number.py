class Solution:
    def countDigits(self, num: int) -> int:
        number = num
        count = 0


        while(number > 0) : 
            last_digit = number % 10
            if(num % last_digit) == 0: 
                count += 1

            number = number // 10
        
        return count
