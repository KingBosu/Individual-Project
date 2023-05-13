class RoiCalculator():
    def __init__(self, Income, Expenses):
        self.Income = Income
        self.Expenses = Expenses

    # Income types that will be contributing to ROI
    class Income(self):
        def __init__(self, rental_income, total_income, storage, misc):
            self.rental_income = rental_income

            self.total_income = 


    #Cost of expenses for the property
    class Expenses(self):
        def __init__(self, taxes, insurance, utilities, hoa_fees, grounds_keeping,vacancy,capital_expenses,property_management, mortgage):
            self.taxes = taxes
            self.insurance = insurance
            self.utilities = utilities
            self.hoa_fees = hoa_fees
            self.grounds_keeping = grounds_keeping
            self.vacancy = vacancy
            self.capital_expenses = capital_expenses
            self.property_management = property_management
            self.mortgage = mortgage
    #income - expenses
    def cashflow(self):
        total_monthly_caseflow = self.Income.total

    #Cash on Cash ROI = what percentage your money is earning
    def cash_roi(self):
        down_payment =[]
        closing_cost =[]
        rehab_budget =[]
        misc_others =[]
        total_investment = sum(down_payment) + sum(closing_cost) + sum(rehab_budget) + sum(misc_others)
        #monthly cash flow * 12 = annual cash flow
        annual_cash_flow = total_monthly_caseflow * 12
        cash_roi = annual_cash_flow / total_investment
        

