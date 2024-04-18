import home_functions as hf
from matplotlib import pyplot as plt
import interest_rate_comp as irc
import rent_vs_buy as rvb
import home_based_on_budget as hbob

print("Hello Homebuying World")

# CLI User input data
#home_price, down_payment, down_payment_percent, interest_rate , loan_term = hf.home_buy_cli()

# Manual Data Hardcoded
home_price = 375_000
down_payment = 75_000
down_payment_percent = 0
interest_rate = 6.5
interest_rate2 = 5
loan_term = 30

# Interest Rate Comparison
irc.rate_comp_plots(home_price, down_payment, interest_rate, interest_rate2, loan_term)

# Rent vs Buy
total_time_years = 30
#total_time_months = 12 * total_time_years

# Rent
monthly_rent = 1655
monthly_utilities = 200
monthly_renters_insurance = 11

# Rent vs Buy Calculation Print Statement
rvb.rent_vs_buy(home_price,down_payment,interest_rate,loan_term,monthly_rent,monthly_utilities,monthly_renters_insurance)


# How much house could you afford based on your current budget
monthly_budget = 2_500

monthly_home_utilities = 200
monthly_home_insurance = 111 # Just a guess
monthly_avg_repair_and_maintenance = 100 # At least this much

home_price_afford = hbob.home_based_on_budget(monthly_budget, interest_rate, loan_term, down_payment, monthly_home_utilities, monthly_home_insurance, monthly_avg_repair_and_maintenance)


