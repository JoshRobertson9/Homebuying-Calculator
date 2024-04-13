import home_functions as hf
from matplotlib import pyplot as plt
import interest_rate_comp as irc

print("Hello Homebuying World")

# CLI User input data
#home_price, down_payment, down_payment_percent, interest_rate , loan_term = hf.home_buy_cli()

# Manual Data Hardcoded
home_price = 375000
down_payment = 75000
down_payment_percent = 0
interest_rate = 5
interest_rate2 = 6.5
loan_term = 30

# Interest Rate Comparison
#irc.rate_comp_plots(home_price, down_payment, interest_rate, interest_rate2, loan_term)

# Rent vs Buy
total_time_years = 30
total_time_months = 12 * total_time_years

# Rent
monthly_rent = 1655
monthly_utilities = 200
monthly_renters_insurance = 11


mortgage_rate = hf.mortgage_rate_calc(home_price, down_payment, interest_rate, loan_term)
print(f"MR: {mortgage_rate}")

rent_sum = 0
buy_diff_sum = 0
monthly_rent_growth = monthly_rent
for i in range(total_time_months):
    rent_sum += monthly_rent_growth
    buy_diff_sum += (mortgage_rate - monthly_rent_growth)
    #print(buy_diff_sum)
    monthly_rent_growth = (1+(0.028/12))*monthly_rent_growth


print(f"Final Rent: {int(monthly_rent_growth)}")

total_rent_cost = rent_sum + total_time_months * (monthly_utilities + monthly_renters_insurance)


# Buy
#monthly_utilities

property_tax_yearly = 0.04 * home_price

# Grass cutting and more
lawn_maintenance_yearly = 150

# Low Estimate
home_repair_yearly = 500

pd = hf.plottable_data(home_price - down_payment, interest_rate, loan_term, mortgage_rate)

monthly_house_expense =  total_time_months*((monthly_renters_insurance*8)  + (monthly_utilities*1.5) )

yearly_house_expense = total_time_years * (property_tax_yearly + lawn_maintenance_yearly + home_repair_yearly)

total_buy_cost = pd[6][total_time_months] + monthly_house_expense + yearly_house_expense


print("Just Costs and House Equity Assessment")
print(f"Years: {total_time_years}")
print(f"Total Rent Cost: {int(total_rent_cost)}")
print(f"Total Buy Cost: {int(total_buy_cost)}")
print(f"Difference: {int(total_rent_cost-total_buy_cost)}")


# Rent Help
down_payment_growth = down_payment * 1.08**total_time_years


# Buy Help
# I saw 3.8% but rounded it down some
house_appreciation = (home_price * (1.035**total_time_years)) - home_price
print(f"House appreciation: {int(house_appreciation)}")

print(f"buydiffsum: {buy_diff_sum}")

print("Total Money Had")
print(f"Years: {total_time_years}")
print(f"Total Rent Scenario: {int(total_rent_cost-down_payment_growth-buy_diff_sum)}")
print(f"Total Buy Scenario: {int(total_buy_cost-house_appreciation)}")
print(f"Difference: {int((total_rent_cost-down_payment_growth-buy_diff_sum)-(total_buy_cost-house_appreciation))}")


