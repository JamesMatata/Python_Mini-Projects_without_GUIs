"""
Mortgage Calculator - Calculate the monthly payments of a fixed-term mortgage over given Nth terms at a given interest rate.
Also, figure out how long it will take the user to pay back the loan. For added complexity, allow users to select 
the compounding interval (Monthly, Weekly, Daily, Continuously).
"""

def get_compounding_intervals():
    """
    Display and get the user's preferred compounding interval.
    """
    intervals = {
        1: "Monthly",
        2: "Weekly",
        3: "Daily",
        4: "Continuous"
    }
    print("\nCompounding Intervals:")
    for key, value in intervals.items():
        print(f"{key}. {value}")

    while True:
        try:
            choice = int(input("Choose a preferred compounding interval (1-4): "))
            if choice in intervals:
                return choice
            else:
                print("ERROR: Please choose a valid option (1-4).")
        except ValueError:
            print("ERROR: Invalid input. Please enter a number between 1 and 4.")

def calculate_installments(principal, years, annual_rate, compounding_option):
    """
    Calculate total payment and installment amount based on the compounding option.
    """
    n=0
    if compounding_option == 1:
        n = 12
    elif compounding_option == 2:
        n = 52
    elif compounding_option == 3:
        n = 365
    elif compounding_option == 4:
        # Using continuous compounding formula: A = P * e^(r * t)
        from math import exp
        total_amount = principal * exp(annual_rate * years)
        return total_amount, total_amount / (12 * years)

    # Regular compounding formula: A = P * (1 + r/n)^(n * t)
    total_amount = principal * (1 + annual_rate / n) ** (n * years)
    return total_amount, total_amount / n

def main():
    print('\n' + "--Mortgage Calculator--".center(80, '#'))

    try:
        principal = float(input("Enter the principal amount (Initial Loan): "))
        years = int(input("Enter the number of years to repay: "))
        annual_rate = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))
    except ValueError:
        print("ERROR: Please enter valid numeric values for all inputs.")
        return

    compounding_option = get_compounding_intervals()
    total_payment, installment = calculate_installments(principal, years, annual_rate, compounding_option)

    intervals = ["Monthly", "Weekly", "Daily", "Continuous"]
    print(f"\nYou selected {intervals[compounding_option - 1]} compounding.")
    print(f"Total Payment: KES. {total_payment:,.2f}")
    if compounding_option != 4:  # Continuous does not have fixed intervals
        print(f"Installment Amount: KES. {installment:,.2f} per installment.")
    else:
        print(f"Installment Amount (estimated as monthly): KES. {installment:,.2f}")

    print('\n'+ '#'.center(80, '#') + '\n\n')

if __name__ == "__main__":
    main()
