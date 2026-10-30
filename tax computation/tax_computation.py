from decimal import Decimal

class TaxReturn:

    #Set instance variables for later methods
    def __init__(self, income, expenses, capital_allowances):
        self.income = income
        self.expenses = expenses
        self.capital_allowances = capital_allowances

        self.profit = 0
        self.personal_allowance = 12570
        self.tax_liability = 0
        self.ni_liability = 0

        self.tax_rates = {
                        "additional_rate_band" : [Decimal('0.45'), 125140],
                        "higher_rate_band" : [Decimal('0.4'), 50270],
                        "basic_rate_band" : [Decimal('0.2'), self.personal_allowance],
                }
        self.ni_rates = {
                "additional_rate" : [Decimal('0.02'), 50270],
                "basic_rate_band" : [Decimal('0.06'), 12570]
            }
        self.basic_band_width = self.tax_rates["higher_rate_band"][1] - self.tax_rates["basic_rate_band"][1]

    #Receives user input, calculates proft before allowances
    def calculate_profit(self):
        self.profit = (self.income - (self.expenses + self.capital_allowances))
        print(f'Your profit is: {self.profit}')
        return self.profit

    #Calculates personal allowance taper where income is above £100,000
    def calculate_allowance(self):
        allowance = self.personal_allowance
        if self.profit > 100000:
            allowance -= (self.profit - 100000) // 2
        if allowance < 0:
            allowance = 0
        self.personal_allowance = allowance
        return self.personal_allowance
    
    #For loop compares taxable profit against tax bands and applies relevant rates
    def calculate_tax(self):
        remaining = self.profit
        self.tax_rates["basic_rate_band"][1] = self.personal_allowance
        self.tax_rates["higher_rate_band"][1] = self.personal_allowance + self.basic_band_width
        for band, value in self.tax_rates.items():
            if remaining >= value[1]:
                self.tax_liability += ((remaining - self.tax_rates[band][1]) * self.tax_rates[band][0])
                remaining -= (remaining - self.tax_rates[band][1])
        print(f'Your Income Tax liability is: {self.tax_liability}')
        return self.tax_liability
    
    #For loop compares taxable profit against NI bands and applies relevant rates
    def calculate_class4_ni(self):
        remaining = self.profit
        for band, value in self.ni_rates.items():
            if remaining >= value[1]:
                self.ni_liability += ((remaining - self.ni_rates[band][1]) * self.ni_rates[band][0])
                remaining -= (remaining - self.ni_rates[band][1])
        print(f'Your Class 4 National Insurance Liability is: {self.ni_liability}')
        return self.ni_liability
    
    #Totals NI and income tax to return user's tax liability based on user inputs
    def total_tax_liability(self):
        self.calculate_profit()
        self.calculate_allowance()
        income_tax = self.calculate_tax()
        ni = self.calculate_class4_ni()
        total_liability = income_tax + ni
        return f'Your total tax liability is {total_liability}'
    
#Request user input for Income, Expenses, and Capital Allowances
while True:
    try:
        income = Decimal(str(input('Enter your income figure: ')))
        break
    except:
        print('Your income must be a number')
while True:
    try:
        expenses = Decimal(str(input('Enter your total expense figure: ')))
        break
    except:
        print('Your expenses must be a number')
while True:   
    try:
        capital_allowances = Decimal(str(input('Enter your Capital Allowance: ')))
        break
    except:
        print('Your capital allowances must be a number')

test = TaxReturn(income, expenses, capital_allowances)
print(test.total_tax_liability())