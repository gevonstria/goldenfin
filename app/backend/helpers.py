from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
import numpy as np

def currency_format(amount):
    return "{:,.2f}".format(amount)

def get_monthly_amortization(term, amount):
    INTEREST_RATE = 0.24;
    monthly_payment = np.pmt(INTEREST_RATE/12, term, amount);
    return round(abs(monthly_payment), 2)

def get_total_interest(amount, monthly_payment, term):
    return round((monthly_payment*term)-amount, 2)

def get_total_sum_upon_maturity(monthly_payment, term):
    return round(monthly_payment*term)

def get_first_loan_payment_date():
    today = datetime.today()

    if today.day in range(1, 15):
        payment_date = datetime(today.year, today.month+1, 7)
    else:
        payment_date = datetime(today.year, today.month+1, 22)

    return datetime.strftime(payment_date, "%B %d, %Y")

def get_loan_maturity_date(date_applied, term):
    three_mon_rel = relativedelta(months=term)
    return datetime.strftime(date_applied +three_mon_rel, "%B %d, %Y")

def loan_summary(loan):
    if loan.loan_type=="A":
        monthly_amortization = get_monthly_amortization(loan.loan_terms, loan.loan_amount)
    else:
        monthly_amortization = loan.loan_amortization
    total_interest = get_total_interest(loan.loan_amount, monthly_amortization, loan.loan_terms)
    total_sum_upon_maturity = get_total_sum_upon_maturity(monthly_amortization, loan.loan_terms)

    data = {
        "principal_amount": currency_format(loan.loan_amount),
        "monthly_amortization": currency_format(monthly_amortization),
        "total_interest": currency_format(total_interest),
        "loan_terms": str(int(loan.loan_terms)),
        "total_sum_upon_maturity": currency_format(total_sum_upon_maturity),
        "first_loan_payment_date": get_first_loan_payment_date(),
        "loan_maturity_date": get_loan_maturity_date(loan.created_at, loan.loan_terms)
    }
    return data