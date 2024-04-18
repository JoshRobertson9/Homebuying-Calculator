

def home_based_on_budget(monthly_budget, interest_rate, loan_term, down_payment, monthly_home_utilities, monthly_renters_insurance, monthly_avg_repair_and_maintenance):

    # Variables
    """
    monthly_budget

    down_payment
    interest_rate
    loan_term
    

    monthly_insurance_cost
    monthly_utility_cost
    property_tax_rate

    mortgage_rate = (home_price - down_payment) * (numerator / denominator)
    
    # Adjustment to add in property tax to the calculation

    mon_bug - (home_price*property_tax)/12 = (home_price - down_payment) * (numerator / denominator)
    
    mon_bug - (home_price*property_tax)/12 = (home_price) * (numerator / denominator) - down_payment * (numerator / denominator)

    mon_bug + down_payment * (numerator / denominator) = (home_price) * (numerator / denominator) + (home_price*property_tax)/12
     
    mon_bug + [down_payment * (numerator / denominator)] = (home_price) * ( (numerator / denominator) + property_tax)/12 )
       
    home_price =  [ mon_bug + [down_payment * (numerator / denominator)] ]    / ( (numerator / denominator) + property_tax)/12 )   

    

    """
    # First version
    
    # Calculate how much you'd have left for your mortgage rate
    mortgage_rate = monthly_budget - monthly_home_utilities - monthly_renters_insurance
    # Re-used from earlier mortgage rate calc but reversed here.
    numerator = (interest_rate/1200)*((1+(interest_rate/1200))**(12*loan_term))
    denominator = ((1+(interest_rate/1200))**(12*loan_term)) - 1

    home_price = mortgage_rate * (denominator/numerator) + down_payment 
    

    # Better version
    """
    mon_bug = monthly_budget - monthly_home_utilities - monthly_renters_insurance

    numerator = (interest_rate/1200)*((1+(interest_rate/1200))**(12*loan_term))
    denominator = ((1+(interest_rate/1200))**(12*loan_term)) - 1
    nd = numerator / denominator

    # property tax rate assumed at 3.6% aka 0.036

    home_price = (mon_bug + (down_payment * nd)) / (nd + (0.036/12))
    """

    print()
    print(f"Based on a monthly budget of ${monthly_budget} you could afford a house worth ${round(home_price,2)} given your other provided parameters.")

    return home_price