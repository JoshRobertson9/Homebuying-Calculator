import locale

# Consolodating the conversion process to a function so that it takes up less space and is easier to manage

def currency_format(value):

    # Printing the result as currency
    locale.setlocale(locale.LC_ALL, 'English_United States.1252')
    conv = locale.localeconv()

    currency_str = locale.format_string("%s%.*f", (conv['currency_symbol'], conv['frac_digits'], abs(value)), grouping=True)
    currency_str = "-" + currency_str if value < 0 else currency_str

    return currency_str