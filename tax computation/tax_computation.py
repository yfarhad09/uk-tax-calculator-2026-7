class TaxReturn:

    personal_allowance = 12570
    basic_rate = 0.2
    basic_rate_band = 37700
    higher_rate = 0.4
    higher_rate_band = 50271
    additional_rate = 0.45
    additional_rate_band = 125141

    #Set instance variables for later methods
    def __init__(self, income, expenses, capital_allowances, profit = 0):
        self.income = income
        self.expenses = expenses
        self.capital_allowances = capital_allowances
        self.profit = profit

    #Receives user input, calculates proft before allowances
    def calculate_profit(self):
        self.profit = self.income - (self.expenses + self.capital_allowances)
        return self.profit
    
    #Takes in profit and deducts personal allowance to calculate taxable income
    def calculate_taxable_profit(self):
        taxable_profit = self.profit - self.personal_allowance
        return taxable_profit
    
    #Elif statements compare taxable profit against tax bands and applies relevant rates
    def calculate_tax(self, taxable_profit):
        tax_liability = 0
        if taxable_profit <= self.personal_allowance:
            tax_liability = 0
        elif taxable_profit > self.additional_rate_band:
            tax_liability += (self.basic_rate_band - self.personal_allowance) * self.basic_rate
            tax_liability += (self.higher_rate_band - self.basic_rate_band) * self.higher_rate
            tax_liability += (taxable_profit - self.additional_rate_band) * self.additional_rate
        elif taxable_profit < self.additional_rate_band and taxable_profit >= self.higher_rate_band:
            tax_liability += (self.basic_rate_band * self.basic_rate)
            tax_liability += (taxable_profit - self.basic_rate_band) * self.higher_rate
        elif taxable_profit >= self.basic_rate_band and taxable_profit <= self.higher_rate_band:
            tax_liability = taxable_profit * self.basic_rate 
        return tax_liability
    
    #Elif statements compare taxable profit against NI bands and applies relevant rates
    def calculate_class4_ni(self, taxable_profit):
        ni_liability = 0
        basic_rate = 0.09
        additional = 0.02
        basic_rate_band = 12570
        upper_limit = 50270
        if taxable_profit > upper_limit:
            ni_liability += (upper_limit - basic_rate_band) * basic_rate
            ni_liability += (taxable_profit - upper_limit) * additional
        elif taxable_profit > basic_rate_band and taxable_profit < upper_limit:
            ni_liability += (taxable_profit - basic_rate_band) * basic_rate
        return ni_liability
    
    #Totals NI and income tax to return user's tax liability based on user inputs
    def total_tax_liability(self):
        self.calculate_profit()
        taxable_profit = self.calculate_taxable_profit()
        income_tax = self.calculate_tax(taxable_profit)
        ni = self.calculate_class4_ni(taxable_profit)
        total_liability = income_tax + ni
        return f'Your total tax liability is {total_liability}'


#Request user input for Income, Expenses, and Capital Allowances
while True:
    try:
        income = float(input('Enter your income figure: '))
        break
    except:
        print('Your income must be a number')
while True:
    try:
        expenses = float(input('Enter your total expense figure: '))
        break
    except:
        print('Your expenses must be a number')
while True:   
    try:
        capital_allowances = float(input('Enter your Capital Allowance: '))
        break
    except:
        print('Your capital allowances must be a number')

test = TaxReturn(income, expenses, capital_allowances)
print(test.calculate_profit())
taxable = test.calculate_taxable_profit()
print(test.calculate_tax(taxable))
print(test.calculate_class4_ni(taxable))
print(test.total_tax_liability())
