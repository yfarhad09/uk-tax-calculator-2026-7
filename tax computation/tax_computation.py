from decimal import Decimal

class TaxReturn:

    personal_allowance = 12570
    basic_rate = Decimal('0.2')
    basic_rate_band = 37700
    higher_rate = Decimal('0.4')
    higher_rate_band = 50271
    additional_rate = Decimal('0.45')
    additional_rate_band = 125141

    #Set instance variables for later methods
    def __init__(self, income, expenses, capital_allowances, profit = 0, taxable_profit = 0):
        self.income = income
        self.expenses = expenses
        self.capital_allowances = capital_allowances
        self.profit = profit
        self.taxable_profit = taxable_profit

    #Receives user input, calculates proft before allowances
    def calculate_profit(self):
        self.profit = (self.income - (self.expenses + self.capital_allowances))
        if self.profit > 100000:
            self.personal_allowance -= (self.profit - 100000) // 2
        print(f'Your profit is: {self.profit}')
        return self.profit
    
    #Takes in profit and deducts personal allowance to calculate taxable income
    def calculate_taxable_profit(self): 
        if self.personal_allowance < 0:
            self.personal_allowance = 0
        self.taxable_profit = self.profit - self.personal_allowance
        if self.taxable_profit <= 0:
            self.taxable_profit = 0
        print(f'Your taxable profit is: {self.taxable_profit}')
        return self.taxable_profit
    
    #Elif statements compare taxable profit against tax bands and applies relevant rates
    def calculate_tax(self):
        tax_liability = 0
        if self.taxable_profit == 0:
            tax_liability = 0
        elif self.taxable_profit > self.additional_rate_band:
            tax_liability += self.basic_rate_band * self.basic_rate
            tax_liability += (self.additional_rate_band - self.basic_rate_band) * self.higher_rate
            tax_liability += (self.taxable_profit - self.additional_rate_band) * self.additional_rate
        elif self.taxable_profit >= self.basic_rate_band:
            tax_liability += (self.basic_rate_band * self.basic_rate)
            tax_liability += (self.taxable_profit - self.basic_rate_band) * self.higher_rate
        else: 
            tax_liability = self.taxable_profit * self.basic_rate
        print(f'Your Income Tax liability is: {tax_liability}')
        return tax_liability
    
    #Elif statements compare taxable profit against NI bands and applies relevant rates
    def calculate_class4_ni(self):
        ni_liability = 0
        basic_rate = Decimal('0.09')
        additional = Decimal('0.02')
        basic_rate_band = 12570
        upper_limit = 50270
        self.taxable_profit = Decimal(str(self.taxable_profit))
        if self.taxable_profit > upper_limit:
            ni_liability += (upper_limit - basic_rate_band) * basic_rate
            ni_liability += (self.taxable_profit - upper_limit) * additional
        elif self.taxable_profit > basic_rate_band and self.taxable_profit < upper_limit:
            ni_liability += (self.taxable_profit - basic_rate_band) * basic_rate
        print(f'Your Class 4 National Insurance Liability is: {ni_liability}')
        return ni_liability
    
    #Totals NI and income tax to return user's tax liability based on user inputs
    def total_tax_liability(self):
        self.calculate_profit()
        taxable_profit = self.calculate_taxable_profit()
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