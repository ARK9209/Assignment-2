# Calculate Factrial Using a Function

def factorial(number):
    if number == 1:   
        return 1
    else:
        fact = number * factorial(number - 1)
        return fact

num = int(input("Enter a number: "))
print(f"Factorial of {num} is: {factorial(num)}")
