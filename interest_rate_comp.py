import home_functions as hf
from matplotlib import pyplot as plt

def rate_comp_plots(home_price, down_payment, interest_rate, interest_rate2, loan_term):

    mortgage_rate = hf.mortgage_rate_calc(home_price, down_payment, interest_rate, loan_term)

    mortgage_rate2 = hf.mortgage_rate_calc(home_price, down_payment, interest_rate2, loan_term)

    # Follow up Calculations
    loan_amount = home_price - down_payment

    # Plottable Data
    pd1 = hf.plottable_data(loan_amount, interest_rate, loan_term, mortgage_rate)
    
    mip, mpp, mtp, months, mte, mts, mtis = pd1

    pd2 = hf.plottable_data(loan_amount, interest_rate2, loan_term, mortgage_rate2)
     
    mip2, mpp2, mtp2, months2, mte2, mts2, mtis2 = pd2

    # Years from Months
    years = []
    for mon in months:
        years.append(mon/12)

    # Plotting
    # Figure 1
    plt.figure(figsize=(10,6))

    # Subplot 1
    plt.subplot(1,2,1)
    plt.title("Loan Amount: $" + "{:,}".format(home_price-down_payment) + "\n"
            + "Interest Rate: " + f"{interest_rate:.2f}"  + "%\n"
            + "Loan Term: " + f"{loan_term} years")
    plt.plot(years, mte, 'b-', label="Cumulative House Equity")
    plt.plot(years, mts, 'r-', label="Total Cumulative Payment")
    plt.plot(years, mtis, 'g-', label="Total Interest Payment (Sunk Cost)")
    plt.xlabel("Years")
#   plt.plot(months, mte, 'b-', label="Cumulative House Equity")
#   plt.plot(months, mts, 'r-', label="Total Cumulative Payment")
#   plt.plot(months, mtis, 'g-', label="Total Interest Payment (Sunk Cost)")
#   plt.xlabel("Months")
    plt.ylabel("$")
    plt.legend()
    plt.grid(True)
    plt.ylim(0, max(max(mts), max(mts2)) + 200000   )

    # Subplot 2
    plt.subplot(1,2,2)
    plt.title("Loan Amount: $" + "{:,}".format(home_price-down_payment) + "\n"
            + "Interest Rate: " + f"{(interest_rate2):.2f}"  + "%\n"
            + "Loan Term: " + f"{loan_term} years")
    plt.plot(years, mte2, 'b-', label="Cumulative House Equity")
    plt.plot(years, mts2, 'r-', label="Total Cumulative Payment")
    plt.plot(years, mtis2, 'g-', label="Total Interest Payment (Sunk Cost)")
    plt.xlabel("Years")
#     plt.plot(months2, mte2, 'b-', label="Cumulative House Equity")
#     plt.plot(months2, mts2, 'r-', label="Total Cumulative Payment")
#     plt.plot(months, mtis2, 'g-', label="Total Interest Payment (Sunk Cost)")
#     plt.xlabel("Months")
    plt.ylabel("$")
    plt.legend()
    plt.grid(True)
    plt.ylim(0, max(max(mts), max(mts2)) + 200000 )

    #plt.show()

    mip_diff = [abs(m2 - m1) for m1, m2 in zip(mtis,mtis2)]


    # Figure 2
    plt.figure()
    #plt.plot(months/12,(mip_diff))
    plt.plot(years,(mip_diff))
    #plt.xlabel("Months")
    plt.xlabel("Years")
    plt.ylabel("Additional Costs ($)")
    plt.title("Additional cumulative cost from higher interest rate")
    plt.show()
