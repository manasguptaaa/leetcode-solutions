def armstrongg_number(number) : 
    original_number = number
    num_digit = len(str(number))
    armstrong_num = 0
    
    while original_number > 0 :
        last_digit = original_number % 10
        armstrong_num = armstrong_num + last_digit ** num_digit
        original_number = original_number // 10
        
    
    return armstrong_num
    

number = int(input("Enter the number : "))
print("The number enter by the user is: - ", number)

result = armstrongg_number(number)

if number == result: 
    print(f"Yes the given number {number} is armstrong number")
else:
    print(f"No the given number {number} is not armstrong number")




