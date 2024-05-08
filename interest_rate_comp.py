import home_functions as hf
from matplotlib import pyplot as plt

def rate_comp_plots(home_price, down_payment, interest_rate, interest_rate2, loan_term):

        
    mortgage_rate = hf.mortgage_rate_calc(home_price, down_payment, interest_rate, loan_term)
    #print(mortgage_rate)

    mortgage_rate2 = hf.mortgage_rate_calc(home_price, down_payment, interest_rate2, loan_term)
    #print(mortgage_rate2)


    # Follow up Calculations
    loan_amount = home_price - down_payment


    # Plottable Data
    pd1 = hf.plottable_data(loan_amount, interest_rate, loan_term, mortgage_rate)
    
    mip, mpp, mtp, months, mte, mts, mtis = pd1

    pd2 = hf.plottable_data(loan_amount, interest_rate2, loan_term, mortgage_rate2)
     
    mip2, mpp2, mtp2, months2, mte2, mts2, mtis2 = pd2

    # Plotting

    plt.figure(figsize=(10,6))
    # plt.title("Hi")

    plt.subplot(1,2,1)
    plt.title("Loan Amount: $" + "{:,}".format(home_price-down_payment) + "\n"
            + "Interest Rate: " + f"{interest_rate:.2f}"  + "%\n"
            + "Loan Term: " + f"{loan_term} years")
    plt.plot(months, mte, 'b-', label="Cumulative House Equity")
    plt.plot(months, mts, 'r-', label="Total Cumulative Payment")
    plt.plot(months, mtis, 'g-', label="Total Interest Payment (Sunk Cost)")
    plt.xlabel("Months")
    plt.ylabel("$")
    plt.legend()
    plt.grid(True)
    plt.ylim(0, max(max(mts), max(mts2)) + 200000   )



    plt.subplot(1,2,2)
    plt.title("Loan Amount: $" + "{:,}".format(home_price-down_payment) + "\n"
            + "Interest Rate: " + f"{(interest_rate2):.2f}"  + "%\n"
            + "Loan Term: " + f"{loan_term} years")
    plt.plot(months2, mte2, 'b-', label="Cumulative House Equity")
    plt.plot(months2, mts2, 'r-', label="Total Cumulative Payment Sunk Cost")
    plt.plot(months, mtis2, 'g-', label="Total Interest Payment Sunk Cost")
    plt.xlabel("Months")
    plt.ylabel("$")
    plt.legend()
    plt.grid(True)
    plt.ylim(0, max(max(mts), max(mts2)) + 200000 )

    #plt.show()

    mip_diff = [abs(m2 - m1) for m1, m2 in zip(mtis,mtis2)]


    plt.figure()
    plt.plot(months,(mip_diff))
    plt.xlabel("Months")
    plt.ylabel("Additional Costs ($)")
    plt.title("Additional cumulative cost from higher interest rate")
    plt.show()

        

