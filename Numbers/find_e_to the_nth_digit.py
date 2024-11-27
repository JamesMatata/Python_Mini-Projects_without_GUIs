"""
Find e to the Nth Digit - Enter a number and have the program generate e up to that many decimal places. 
Keep a limit to how far the program will go.
"""

from decimal import Decimal, getcontext

# Function to calculate e using Taylor series
def calculate_e(precision):
    e = Decimal(0)
    factorial = 1
    for i in range(precision + 10):  # Extra terms for better precision
        if i > 0:
            factorial *= i
        e += Decimal(1) / Decimal(factorial)
    return e

# Input for decimal places
decimal_places = int(input('Enter the number of decimals: '))

# Set precision (limit precision to 100 to prevent excessive computation)
if decimal_places <= 100:
    getcontext().prec = decimal_places + 5

    # Calculate e
    e = calculate_e(decimal_places)

    # Format the result to the desired decimal places
    target_format = Decimal('1.' + '0' * decimal_places)
    rounded_e = e.quantize(target_format)
    
    print(rounded_e)
else:
    print("Please enter a value less than 100.")
