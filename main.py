import home_functions as hf
from matplotlib import pyplot as plt
import interest_rate_comp as irc
import rent_vs_buy as rvb

print("Hello Homebuying World")

# CLI User input data
#home_price, down_payment, down_payment_percent, interest_rate , loan_term = hf.home_buy_cli()

# Manual Data Hardcoded
home_price = 375_000
down_payment = 75_000
down_payment_percent = 0
interest_rate = 5
interest_rate2 = 6.5
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


