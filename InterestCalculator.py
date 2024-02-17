# This program calculates the accrued interest on an account using a counted loop.

def calculate_accrued_interest(principal, rate, periods_per_year, duration):
    """
    Calculate the accrued interest on an account.

    Args:
    principal (float): The initial amount of money.
    rate (float): The yearly interest rate as a decimal number.
    periods_per_year (int): The number of compounding periods in a year.
    duration (int): The number of years for which the interest is calculated.

    Returns:
    float: The principal value at the end of the duration.
    """
    # Calculate the interest on each compounding period
    for year in range(duration):
        for period in range(periods_per_year):
            principal = principal * (1 + rate / periods_per_year)
    return principal


def main():
    # Get user input
    principal = float(input("Enter the principal amount: $"))
    rate = float(input("Enter the yearly interest rate as a decimal number: "))
    periods_per_year = int(input("Enter the number of compounding periods in a year: "))
    duration = int(input("Enter the duration in years: "))

    # Calculate accrued interest
    final_principal = calculate_accrued_interest(principal, rate, periods_per_year, duration)

    # Display the result
    print(f"The principal value at the end of {duration} years is: ${final_principal:.2f}")


if __name__ == "__main__":
    main()
