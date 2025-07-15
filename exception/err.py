
n = 10
try : 
    res =n /0 
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
    
#ZeroDivisionError is a built-in exception that occurs when you attempt to divide a number by zero, which is mathematically undefined. Python raises this 
#exception when the right operand (divisor) in a division or modulo operation is zero.