from decimal import Decimal

import home_functions as hf
from matplotlib import pyplot as plt
import interest_rate_comp as irc
import rent_vs_buy as rvb
import home_based_on_budget as hbob

def main():
    print("Hello Homebuying World\n")
    print("What would you like to calculate for making a home purchase?")
    print("1. Interest Rate Comparison")
    print("2. Rent vs Buy")
    print("3. How much home can you afford based on your budget")
    choice = int(input("Provide the number of the choice that you want: "))
    print()

    # CLI User input data
    home_price, down_payment, down_payment_percent, interest_rate , loan_term = hf.home_buy_cli()

    # Manual Data Hardcoded Overwrite
    # home_price = 375_000
    # down_payment = 75_000
    # down_payment_percent = 0
    # interest_rate = 6.5
    # loan_term = 30

    match choice:

        # Interest Rate Comparison
        case 1:

            # Interest Rate 2
            while True:
                try:
                    interest_rate2 = Decimal(input("What is the second interest rate that you have? (Ex. 7 for 7%) "))
                    break
                except ValueError:
                    print("Invalid input. Try again.")

            print("Your interest rate is: " + f"{interest_rate2:.2f}"  + "%.\n")

            print("Here are you comparison plots")
            irc.rate_comp_plots(home_price, down_payment, interest_rate, interest_rate2, loan_term)

        # Rent vs Buy
        case 2:
            total_time_years = 30
            #total_time_months = 12 * total_time_years

            # Rent
            monthly_rent = Decimal(1655)
            monthly_utilities = Decimal(200)
            monthly_renters_insurance = Decimal(11)

            # Rent vs Buy Calculation Print Statement
            rvb.rent_vs_buy(home_price,down_payment,interest_rate,loan_term,monthly_rent,monthly_utilities,monthly_renters_insurance)

        # How much house could you afford based on your current budget
        case 3:
            monthly_budget = 2_500

            # Amounts in $
            monthly_home_utilities = 200 # Just a estimated guess
            monthly_home_insurance = 111 # Just a estimated guess
            monthly_avg_repair_and_maintenance = 100 # At least this much

            home_price_afford = hbob.home_based_on_budget(monthly_budget, interest_rate, loan_term, down_payment, monthly_home_utilities, monthly_home_insurance, monthly_avg_repair_and_maintenance)

if __name__ == "__main__":
    main()