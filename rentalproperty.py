
# Income types that will be contributing to ROI
class Income:
    def __init__(self, rental_income, storage, misc):
        self.rental_income = rental_income
        self.storage = storage
        self.misc = misc
        self.total_income = sum(self.rental_income) + sum(self.storage) + sum(misc)

    # Cost of expenses for the property


class Expenses:
    def __init__(self, taxes, insurance, utilities, hoa_fees, grounds_keeping, vacancy, capital_expenses, property_management, mortgage):
        self.taxes = taxes
        self.insurance = insurance
        self.utilities = utilities
        self.hoa_fees = hoa_fees
        self.grounds_keeping = grounds_keeping
        self.vacancy = vacancy
        self.capital_expenses = capital_expenses
        self.property_management = property_management
        self.mortgage = mortgage
        self.total_expenses = sum(self.taxes + self.insurance + self.utilities + hoa_fees + grounds_keeping + vacancy + capital_expenses + property_management + mortgage)


class RoiCalculator:
    def __init__(self):
        self.Income = self.total_income
        self.Expenses = self.total_expenses

    # income - expenses
    def cashflow(self):
        self.total_monthly_cashflow = self.Income.total - self.Expenses.total
        self.annual_cash_flow = self.total_monthly_cashflow * 12
        return self.annual_cash_flow

    # Cash on Cash ROI = what percentage your money is earning
    def cash_roi(self):
        down_payment = []
        closing_cost = []
        rehab_budget = []
        misc_others = []
        total_investment = sum(down_payment) + sum(closing_cost) + \
            sum(rehab_budget) + sum(misc_others)
        cash_roi = (self.annual_cash_flow // total_investment) * 100
        return cash_roi
    
    def run_roi_calculator():
    
        rental_income = [1000, 2000, 1200]
        storage_income = [0, 0, 100]
        misc_income = [50, 0, 100]
        income = Income(rental_income, storage_income, misc_income)

        taxes = 1000
        insurance = 500
        utilities = 300
        hoa_fees = 0
        grounds_keeping = 200
        vacancy = 250
        capital_expenses = 150
        property_management = 300
        mortgage = 1500
        expenses = Expenses(taxes, insurance, utilities, hoa_fees, grounds_keeping, vacancy, capital_expenses, property_management, mortgage)

        roi_calculator = RoiCalculator(income, expenses)
        monthly_cashflow = roi_calculator.cashflow()
        cash_roi = roi_calculator.cash_roi()

    print("Monthly cash flow: $", self.total_monthly_cashflow)
    print("Cash on cash ROI: {:.2f}%".format(cash_roi))
