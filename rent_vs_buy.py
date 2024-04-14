import home_functions as hf

# Rent vs Buy

 # over time duration

# Rent Sunk Cost
    # Monthly Rent
    # Monthly Utilities
    # Renter's Insurance


# Buy Sunk Cost
    # Yearly Tax Cost
    # Interest Cost
    # Utilities Cost
    # Home maintenance Cost
    # Home Care Costs


# Solve for
"""
How much you could rent for and still break even

How much house you could afford based on what you are renting now.

What year do you break even

"""

# Renting Costs
# [monthly_rent, monthly_utilities, monthly_renter_insurance]

# Buy 

#def rent_vs_buy([],[]):

def rent_vs_buy(home_price, down_payment, interest_rate,total_time_years,monthly_rent,monthly_utilities,monthly_renters_insurance):

    mortgage_rate = hf.mortgage_rate_calc(home_price, down_payment, interest_rate,total_time_years)
    #print(f"MR: {mortgage_rate}")

    total_time_months = 12 * total_time_years

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

    pd = hf.plottable_data(home_price - down_payment, interest_rate, total_time_years, mortgage_rate)

    monthly_house_expense =  total_time_months*((monthly_renters_insurance*8)  + (monthly_utilities*1.5) )

    yearly_house_expense = total_time_years * (property_tax_yearly + lawn_maintenance_yearly + home_repair_yearly)

    total_buy_cost = pd[6][total_time_months] + monthly_house_expense + yearly_house_expense


    print()
    print("Just Costs and House Equity Assessment")
    print(f"Years: {total_time_years}")
    print(f"Total Rent Cost: {int(total_rent_cost)}")
    print(f"Total Buy Cost: {int(total_buy_cost)}")
    print(f"Difference: {int(total_rent_cost-total_buy_cost)}")
    print()

    # Rent Help
    down_payment_growth = down_payment * 1.08**total_time_years

    # Buy Help
    # I saw 3.8% but rounded it down some
    house_appreciation = (home_price * (1.035**total_time_years)) - home_price
    print(f"House appreciation: {int(house_appreciation)}")

    print(f"buydiffsum: {buy_diff_sum}")
    
    print()
    print("Total Money Had")
    print(f"Years: {total_time_years}")
    print(f"Total Rent Scenario: {int(total_rent_cost-down_payment_growth-buy_diff_sum)}")
    print(f"Total Buy Scenario: {int(total_buy_cost-house_appreciation)}")
    print(f"Difference: {int((total_rent_cost-down_payment_growth-buy_diff_sum)-(total_buy_cost-house_appreciation))}")


