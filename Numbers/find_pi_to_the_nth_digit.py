"""
Find PI to the Nth Digit - Enter a number and have the program generate π (pi) up to that many decimal places. 
Keep a limit to how far the program will go.
"""

from decimal import Decimal, getcontext
import math

num = int(input("Enter the number of decimal places you want to calculate pI to: "))

if num > 100:
    print("The number you entered is too large. Please enter a number less than 100.")

else:
    getcontext().prec = num + 5

    pi = Decimal(math.pi)

    target_format = Decimal('1.' + '0' * num)

    rounded_pi = pi.quantize(target_format)

    print(rounded_pi)