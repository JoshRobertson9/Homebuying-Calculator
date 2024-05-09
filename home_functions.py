import locale
from decimal import Decimal

# Homebuying inputs received through the command-line interface
def home_buy_cli():

    locale.setlocale(locale.LC_ALL, '')

    # Home Price
    while True:
        try:
            home_price = Decimal(input("How expensive of a home do you plan to buy? "))
            #home_price_comma = "{:,}".format(home_price)
            #print(home_price_comma)
            #print(f"Your home price is: ${home_price:.2f}")
            # other print option
            # print("Your home price is: $" + "{:,}".format(home_price))
            formatted_home_price = locale.currency(home_price, grouping=True)
            print("Your home price is:", formatted_home_price)

            break
        except ValueError:
            print("There's an error with the home price. Try again. Just the number is needed, no special characters.")

    # Downpayment
    while True:
        try:
            choice_dp = Decimal(input("Do you want provide the downpayment as an amount (option 1) or a percentage (option 2)? "))
        except ValueError:
            choice_dp = 0

        # Downpayment as an amount
        if choice_dp == 1:
            try:
                down_payment = Decimal(input("How much downpayment do you want to put down as an amount? "))
                break
            except:
                print("Invalid input. Try again.")

        # Downpayment as a percentage
        elif choice_dp == 2:
            try:
                down_payment = (Decimal(input("how much downpayment do you want to put down as a percentage? ")) / 100) * home_price
                break
            except:
                print("Invalid input. Try again.")
                #down_payment = 0

        else:
            print("No down payment option selected. Try again.")

    down_payment_percent = (down_payment/home_price)*100

    # Old display option
    #print("Your down payment is: $" + "{:,}".format(down_payment) + ". Which is " + f"{down_payment_percent:.2f}"  + "%." )
    formatted_down_payment = locale.currency(down_payment, grouping=True)
    print(f"Your down payment is: {formatted_down_payment}. Which is {down_payment_percent:.2f}%.")

    # Interest Rate
    while True:
        try:
            interest_rate = Decimal(input("What interest rate do you have? (Ex. 7 for 7%) "))
            break
        except ValueError:
            print("Invalid input. Try again.")

    print("Your interest rate is: " + f"{interest_rate:.2f}"  + "%." )


    # Term of the loan
    while True:
        try:
            loan_term = int(input("What is the term of the loan that you are considering in years? "))
            print("Your loan term is: " + f"{loan_term}" + " years.")
            break
        except ValueError:
            print("There's an error with loan term you provide. Just the number in years is needed, no special characters.")

    return home_price, down_payment, down_payment_percent, interest_rate , loan_term

# Mortgage Rate Calculation
def mortgage_rate_calc(home_price, down_payment, interest_rate, loan_term):
    # Assumptions that should be handled by earlier inputs
        # All values are greater than 0.
        # All values are numbers.
        # home_price >= down_payment.

    if interest_rate == 0:
        mortgage_rate = (home_price - down_payment) / (12*loan_term)
        
    elif loan_term == 0:
        # Could improve the else eqn to just handle this scenario on its own
        mortgage_rate = (home_price - down_payment)
    
    else :
        numerator = (interest_rate/1200)*((1+(interest_rate/1200))**(12*loan_term))

        denominator = ((1+(interest_rate/1200))**(12*loan_term)) - 1
    
        mortgage_rate = (home_price - down_payment) * (numerator / denominator)

    return mortgage_rate


# Interest and Principal payment calculation for an amortization schedule
def interest_payment(current_balance, rate, term, mortgage_rate):
    
    monthly_interest_payment = current_balance * ((rate/100)/12)

    monthly_principal_payment = mortgage_rate - monthly_interest_payment

    # The long way to calculate the above.
    # monthly_principal_payment =  (((current_balance * ((rate/100)/12))*((1 + (rate/100)/12)**(term*12))) / ((1 + ((rate/100)/12))**(term*12)-1))  - monthly_interest_payment

    return monthly_interest_payment, monthly_principal_payment


# Plottable Data
def plottable_data(principal, annual_interest_rate, loan_term_years,mortgage_rate):

    monthly_interest_payment = [0]
    monthly_principal_payment = [0]
    monthly_total_payment = [0]
    months = [0]
    monthly_total_equity = [0]
    monthly_total_spend = [0]
    monthly_total_interest_spend = [0]

    remaining_balance = principal

    for n in range((loan_term_years*12)):

        ip,pp = interest_payment(remaining_balance,annual_interest_rate,loan_term_years-(n/12),mortgage_rate)

        remaining_balance -= pp

        # Appending
        monthly_interest_payment.append(ip)

        monthly_principal_payment.append(pp)

        monthly_total_payment.append(ip + pp)

        months.append(n+1)

        monthly_total_equity.append(sum(monthly_principal_payment))

        monthly_total_spend.append(sum(monthly_interest_payment)+sum(monthly_principal_payment))

        monthly_total_interest_spend.append(sum(monthly_interest_payment))

    pd = [
        monthly_interest_payment,
        monthly_principal_payment,
        monthly_total_payment,
        months,
        monthly_total_equity,
        monthly_total_spend,
        monthly_total_interest_spend
        ]

    #return monthly_interest_payment, monthly_principal_payment, monthly_total_payment, months, monthly_total_equity, monthly_total_spend, monthly_total_interest_spend
    return pd


if __name__ == "__main__":
    home_buy_cli()



