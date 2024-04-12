import home_functions as hf
from matplotlib import pyplot as plt
import interest_rate_comp as irc

print("Hello Homebuying World")

# CLI User input data
home_price, down_payment, down_payment_percent, interest_rate , loan_term = hf.home_buy_cli()

# Manual Data Hardcoded
#home_price = 400000
#down_payment = 0
#down_payment_percent = 0
#interest_rate = 7
interest_rate2 = 5
#loan_term = 30

irc.rate_comp_plots(home_price, down_payment, interest_rate, interest_rate2, loan_term)


