try:
    n = 10
    res = n / 0
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid value encountered.")
else:
    print("No exceptions occurred, result is:", res)
finally:
    print("Execution completed, whether an exception occurred or not finallyt block.")