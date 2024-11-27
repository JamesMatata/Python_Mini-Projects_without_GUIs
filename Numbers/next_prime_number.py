"""
Next Prime Number - Have the program find prime numbers until the user chooses to stop asking for the next one.
"""

get_next_prime = True

def is_prime(num):
    if num<2:
        return False
    for n in range(2,num):
        if num%n == 0:
            return False
    return True

def next_prime(prime):
    num = prime + 1
    not_found = True
    while not_found:
        if is_prime(num):
            not_found = False
            return num       
        else:
            num+=1

def ask_for_next(number):
    number = number
    while get_next_prime:
        get_next = input('Do you want the next prime number(yes/no): ').strip().lower()
        if get_next == 'yes':
            number = next_prime(number)
            print(number)
        else:
            break
        

number = int(input('Enter a number of your choice: '))
if is_prime(number):
    print(number)
    ask_for_next(number)
else:
    number = next_prime(number)
    print(number)
    ask_for_next(number)



