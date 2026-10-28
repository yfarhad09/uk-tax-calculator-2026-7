from decimal import Decimal

class TaxReturn:

    tax_rates = {
                "additional_rate_band" : [Decimal('0.45'), 125140],
                "higher_rate_band" : [Decimal('0.4'), 50270],
                "basic_rate_band" : [Decimal('0.2'), 12570]
        }

    ni_rates = {
        "basic_rate_band" : [Decimal('0.09'), 12570],
        "additional_rate" : [Decimal('0.02'), 50270]
    }

    #Set instance variables for later methods
    def __init__(self, income, expenses, capital_allowances, tax_liability = 0, ni_liability = 0, profit = 0, personal_allowance = 12570, tax_rates):
        self.income = income
        self.expenses = expenses
        self.capital_allowances = capital_allowances
        self.profit = profit
        self.personal_allowance = personal_allowance
        self.tax_liability = tax_liability
        self.ni_liability = ni_liability
        self.tax_rates = tax_rates

    #Receives user input, calculates proft before allowances
    def calculate_profit(self):
        self.profit = (self.income - (self.expenses + self.capital_allowances))
        if self.profit > 100000:
            self.personal_allowance -= (self.profit - 100000) // 2
        print(f'Your profit is: {self.profit}')
        return self.profit
    
    
    #Elif statements compare taxable profit against tax bands and applies relevant rates
    def calculate_tax(self):
        taxable_profit = self.profit - self.personal_allowance
        for band, value in self.tax_rates.items():
            if taxable_profit > value[1]:
                tax_liability += (taxable_profit * value[0])
                taxable_profit -= (taxable_profit - self.tax_rates[value[1]]
        print(f'Your Income Tax liability is: {tax_liability}')
        return self.tax_liability
    
    #Elif statements compare taxable profit against NI bands and applies relevant rates
    def calculate_class4_ni(self):
        if self.profit > self.ni_rates['upper_limit']:
            self.ni_liability += (self.ni_rates['upper_limit'] - self.ni_rates['basic_rate_band']) * self.ni_rates['basic_rate']
            self.ni_liability += (self.profit - self.ni_rates['upper_limit'] * self.ni_rates['additional'])
        elif self.profit > self.ni_rates['basic_rate_band'] and self.profit < self.ni_rates['upper_limit']:
            self.ni_liability += (self.profit - self.ni_rates['basic_rate_band'] * self.ni_rates['basic_rate'])
        print(f'Your Class 4 National Insurance Liability is: {self.ni_liability}')
        return self.ni_liability
    
    #Totals NI and income tax to return user's tax liability based on user inputs
    def total_tax_liability(self):
        self.calculate_profit()
        taxable_profit = self.calculate_profit() - self.personal_allowance
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