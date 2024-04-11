from matplotlib import pyplot as plt

print("Hello Homebuying World")

"""
# Home Price
while True:
    try:
        home_price = float(input("How expensive of a home do you plan to buy? "))
        #home_price_comma = "{:,}".format(home_price)
        #print(home_price_comma)
        #print(f"Your home price is: ${home_price:.2f}")
        print("Your home price is: $" + "{:,}".format(home_price))

        break
    except ValueError:
        print("There's an error with the home price. Try again. Just the number is needed, no special characters.")


# Downpayment
while True:
    try:
        choice_dp = float(input("Do you want provide the downpayment as an amount (option 1) or a percentage (option 2)? "))
    except ValueError:
        choice_dp = 0

    # Downpayment as an amount
    if choice_dp == 1:
        try:
            down_payment = float(input("How much downpayment do you want to put down as an amount? "))
            break
        except:
            print("Invalid input. Try again.")

    # Downpayment as a percentage
    elif choice_dp == 2:
        try:
            down_payment = (float(input("how much downpayment do you want to put down as a percentage? ")) / 100) * home_price
            break
        except:
            print("Invalid input. Try again.")
            #down_payment = 0

    else:
        print("No down payment option selected. Try again.")

down_payment_percent = (down_payment/home_price)*100

print("Your down payment is: $" + "{:,}".format(down_payment) + ". Which is " + f"{down_payment_percent:.2f}"  + "%." )

# Interest Rate
while True:
    try:
        interest_rate = float(input("What interest rate do you have? (Ex. 7 for 7%) "))
        break
    except ValueError:
        print("Invalid input. Try again.")

print("Your interest rate is: " + f"{interest_rate:.2f}"  + "%." )


# Term of the loan
while True:
    try:
        loan_term = int(input("What is the term of the loan that you are considering? "))
        print("Your loan term is: " + f"{loan_term}" + " years.")
        break
    except ValueError:
        print("There's an error with loan term you provide. Just the number in years is needed, no special characters.")

"""


# Manual Data Hardcoded
home_price = 400000
down_payment = 0
down_payment_percent = 0
interest_rate = 7
loan_term = 30

interest_rate2 = 9

# Follow up Calculations

loan_amount = home_price - down_payment
monthly_rate = interest_rate / 12

# Old
#monthly_rate = 12 * (interest_rate + 1)**(1/12)
#monthly_rate = (1 + (interest_rate/12))**12 - 1
#print("Monthly Rate: ",monthly_rate)

#mortgage_rate = 2661.21


def mortgage_rate_calc(home_price, down_payment, interest_rate, loan_term):

    numerator = (interest_rate/1200)*((1+(interest_rate/1200))**(12*loan_term))

    denominator = ((1+(interest_rate/1200))**(12*loan_term)) - 1

    mortgage_rate = (home_price - down_payment) * (numerator / denominator)

    return mortgage_rate


mortgage_rate = mortgage_rate_calc(home_price, down_payment, interest_rate, loan_term)

#print(mortgage_rate)


def interest_payment(current_balance,rate,term,mr):
    
    ip = current_balance * ((rate/100)/12)

    pp = mortgage_rate - ip

    pp =  (((current_balance * ((rate/100)/12))*((1 + (rate/100)/12)**(term*12))) / (   (1 + ((rate/100)/12))**(term*12)  -1    ) )   - ip

    return ip, pp




"""
i,p = interest_payment(loan_amount,interest_rate,loan_term,mortgage_rate)

print(i)
print(p)

i,p = interest_payment(loan_amount-p,interest_rate,loan_term-(1/12),mortgage_rate)

print(i)
print(p)
"""

def plot_data(principal, annual_interest_rate, loan_term_years,mortgage_rate):

    monthly_interest_payment = [0]
    monthly_principal_payment = [0]
    monthly_total_payment = [0]
    months = [0]
    monthly_total_equity = [0]
    monthly_total_spend = [0]
    monthly_total_interest_spend = [0]

    remaining_balance = principal

    for n in range((loan_term_years*12)):

        i,p = interest_payment(remaining_balance,annual_interest_rate,loan_term_years-(n/12),mortgage_rate)

        remaining_balance -= p

        monthly_interest_payment.append(i)
        monthly_principal_payment.append(p)
        monthly_total_payment.append(i+p)
        months.append(n+1)
        monthly_total_equity.append(sum(monthly_principal_payment))
        monthly_total_spend.append(sum(monthly_interest_payment)+sum(monthly_principal_payment))
        monthly_total_interest_spend.append(sum(monthly_interest_payment))



    return monthly_interest_payment, monthly_principal_payment, monthly_total_payment, months, monthly_total_equity, monthly_total_spend, monthly_total_interest_spend


#Plotting

mip, mpp, mtp, months, mte, mts, mtis = plot_data(loan_amount, interest_rate, loan_term, mortgage_rate)


mortgage_rate2 = mortgage_rate_calc(home_price, down_payment, interest_rate2, loan_term)
#print(mortgage_rate2)

mip2, mpp2, mtp2, months2, mte2, mts2, mtis2 = plot_data(loan_amount, interest_rate2, loan_term, mortgage_rate2)

"""
plt.figure()
plt.plot(months, mpp)
plt.xlabel("Months")
plt.ylabel("Principal Payment")
plt.grid(True)
plt.show()
"""

plt.figure(figsize=(10,5))

plt.subplot(1,2,1)
plt.title("Loan Amount: $" + "{:,}".format(home_price-down_payment) + "\n" + "Interest Rate: " + f"{interest_rate:.2f}"  + "%")
plt.plot(months, mte, 'b-', label="1")
plt.plot(months, mts, 'r-', label="2")
plt.xlabel("Months")
plt.ylabel("$")
plt.grid(True)
plt.ylim(0, max(max(mts), max(mts2)) + 200000   )



plt.subplot(1,2,2)
plt.title("Loan Amount: $" + "{:,}".format(home_price-down_payment) + "\n" + "Interest Rate: " + f"{(interest_rate2):.2f}"  + "%")
plt.plot(months2, mte2, 'b-', label="1")
plt.plot(months2, mts2, 'r-', label="2")
plt.xlabel("Months")
plt.ylabel("$")
plt.grid(True)
plt.ylim(0, max(max(mts), max(mts2)) + 200000 )


#plt.tight_layout()
#plt.show()

mip_diff = [m2 - m1 for m1, m2 in zip(mtis,mtis2)]

plt.figure()
plt.plot(months,(mip_diff))
plt.xlabel("Months")
plt.ylabel("Additional Costs ($)")
plt.title("Additional cumulative cost from higher interest rate")
plt.show()

