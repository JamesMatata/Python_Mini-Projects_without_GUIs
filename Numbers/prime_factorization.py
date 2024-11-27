"""
Prime Factorization - Have the user enter a number and find all Prime Factors (if there are any) and display them.
"""

number = int(input("Enter a number to find its prime factors: "))

def prime_factors(number):
    factors = []

    n = 2

    while n <= number:
        if number % n == 0:
            factors.append(n)
            number = number / n

        else:
            n += 1

    return factors

print(prime_factors(number))