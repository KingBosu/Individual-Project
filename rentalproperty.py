

class Income:
    """
    Income related to the property that will be contributing to ROI
       
    """
    def __init__(self, rental_income, storage, misc):
        self.total_income = sum(rental_income) + \
            sum(storage) + sum(misc)



class Expenses:
    """
    Expenses related to the property that will be contributing to ROI
        
    """
    def __init__(self, taxes, insurance, utilities, hoa_fees, grounds_keeping, vacancy, capital_expenses, property_management, mortgage):
        self.total_expenses = (taxes + insurance + utilities + hoa_fees +
                               grounds_keeping + vacancy + capital_expenses + property_management + mortgage)


class RoiCalculator:
    """
    RoiCalculator calculates the ROI for the property by using the data inputted in the other two classes.

    """
    def __init__(self, income, expenses):
        
        self.total_income = income
        self.total_expenses = expenses

    
    def cashflow(self):
        """
        Calculates the cash the property is bringing in.
        """
        self.total_monthly_cashflow = self.total_income - self.total_expenses
        self.annual_cash_flow = self.total_monthly_cashflow * 12
        return self.annual_cash_flow

    
    def cash_roi(self, down_payment, closing_cost, rehab_budget, misc_others):
        """
        Cash on Cash ROI = what percentage your money is earning
        
        """
        total_investment = down_payment + closing_cost + rehab_budget + misc_others
        cash_roi = (self.annual_cash_flow / total_investment) * 100
        return cash_roi


def run_roi_calculator():
    """
    Runs the roi calculator.
    """
    rental_income = [1000, 2000, 1200]
    storage_income = [0, 0, 100]
    misc_income = [50, 0, 100]
    income = Income(rental_income, storage_income, misc_income)
    total_income = income.total_income

    taxes = 1000
    insurance = 500
    utilities = 300
    hoa_fees = 0
    grounds_keeping = 200
    vacancy = 250
    capital_expenses = 150
    property_management = 300
    mortgage = 1500
    expenses = Expenses(taxes, insurance, utilities, hoa_fees, grounds_keeping,
                        vacancy, capital_expenses, property_management, mortgage)
    total_expenses = expenses.total_expenses

    roi_calculator = RoiCalculator(total_income, total_expenses)
    monthly_cashflow = roi_calculator.cashflow()
    cash_roi = roi_calculator.cash_roi(50000, 500, 1000, 100)
    roi_calculator.total_monthly_cashflow

    print("Monthly cash flow: $", monthly_cashflow)
    print("Cash on cash ROI: {:.2f}%".format(cash_roi))


run_roi_calculator()
