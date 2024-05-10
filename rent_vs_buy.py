from matplotlib import pyplot as plt
from matplotlib.ticker import FuncFormatter

import home_functions as hf
from decimal import Decimal

from currency_format import currency_format

# Rent vs Buy Notes
# Solve for
"""
How much you could rent for and still break even

How much house you could afford based on what you are renting now.

What year do you break even
"""

# Rent Sunk Costs
    # Monthly Rent
    # Monthly Utilities
    # Renter's Insurance

# Buy Sunk Costs
    # Yearly Tax Cost
    # Interest Cost
    # Utilities Cost
    # Home maintenance Cost
    # Home Care Costs


def rent_vs_buy(home_price, down_payment, interest_rate,total_time_years,monthly_rent,monthly_utilities,monthly_renters_insurance):

    mortgage_rate = hf.mortgage_rate_calc(home_price, down_payment, interest_rate,total_time_years)
    mr_str = currency_format(mortgage_rate)
    print(f"\nMortgage Rate: {mr_str}")

    total_time_months = 12 * total_time_years

    rent_sum = Decimal(0)
    buy_diff_sum = Decimal(0)
    monthly_rent_growth = monthly_rent
    for i in range(total_time_months):
        rent_sum += monthly_rent_growth
        buy_diff_sum += (mortgage_rate - monthly_rent_growth)
        #print(buy_diff_sum)
        monthly_rent_growth = Decimal(1+(0.028/12))*monthly_rent_growth


    mrg_str = currency_format(monthly_rent_growth)
    print(f"\nFinal Rent: {mrg_str}")

    total_rent_cost = rent_sum + total_time_months * (monthly_utilities + monthly_renters_insurance)

    # Buy
    #monthly_utilities

    property_tax_yearly = Decimal(0.04) * home_price

    # Grass cutting and more
    lawn_maintenance_yearly = Decimal(150)

    # Low Estimate
    home_repair_yearly = Decimal(500)

    pd = hf.plottable_data(home_price - down_payment, interest_rate, total_time_years, mortgage_rate)

    monthly_house_expense =  total_time_months * ((monthly_renters_insurance * 8)  + (monthly_utilities * Decimal(1.5)) )

    yearly_house_expense = total_time_years * (property_tax_yearly + lawn_maintenance_yearly + home_repair_yearly)

    total_buy_cost = pd[6][total_time_months] + monthly_house_expense + yearly_house_expense

    print()
    print("Just Costs and House Equity Assessment")
    print(f"Years: {total_time_years}")

    trc_str = currency_format(total_rent_cost)
    print(f"Total Rent Cost: {trc_str}")

    tbc_str = currency_format(total_buy_cost)
    print(f"Total Buy Cost: {tbc_str}")

    diff_str = currency_format(total_rent_cost - total_buy_cost)
    print(f"Difference: {diff_str}")
    print()

    # Rent Help
    down_payment_growth = down_payment * Decimal(1.08)**total_time_years

    # Buy Help
    # I saw 3.8% but rounded it down some to 3.5%
    house_appreciation = (home_price * (Decimal(1.035)**total_time_years)) - home_price

    ha_str = currency_format(house_appreciation)
    print(f"House appreciation: {ha_str}")

    bds_str = currency_format(buy_diff_sum)
    print(f"buydiffsum: {bds_str}")


    # Final Results    
    print()
    print(f"Total Money after {total_time_years} years")

    overall_rent_cost = (total_rent_cost - down_payment_growth - buy_diff_sum)
    trs_str = currency_format(overall_rent_cost)
    print(f"Total Rent Scenario: {trs_str}")

    overall_buy_cost = (total_buy_cost - house_appreciation)
    tbs_str = currency_format(overall_buy_cost)
    print(f"Total Buy Scenario: {tbs_str}")

    total_diff = (total_rent_cost - down_payment_growth - buy_diff_sum) - (total_buy_cost - house_appreciation)
    total_diff_str = currency_format(total_diff)
    print(f"Difference: {total_diff_str}")

    # Bar Chart
    options = ["Rent Scenario", "Buy Scenario"]
    values = [overall_rent_cost, overall_buy_cost]

    bar_width = .75
    bar_spacing = 2
    total_width = (bar_width + bar_spacing) * 2

    plt.figure(figsize=(total_width, 6))
    plt.bar(options, values, width=bar_width)

    plt.xlabel("Categories")
    plt.ylabel("Total Value ($)")
    plt.title(f"Total Money after {total_time_years} years")

    def format_thousands(y, pos):
        return '{:,.0f}'.format(y)

    formatter = FuncFormatter(format_thousands)
    plt.gca().yaxis.set_major_formatter(formatter)

    plt.show()
