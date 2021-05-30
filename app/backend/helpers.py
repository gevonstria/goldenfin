from django.conf import settings
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from django.core.mail import EmailMultiAlternatives
from backend.models import LoanDetails, Customer
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

def send_email(loan_data):
    
    customer = Customer.objects.filter(loan__id=loan_data["loan_id"]).first()
    table_html = "<table>"
    table_html += "<tr>";
    table_html += "<td>Principal Amount</td>";
    table_html += "<td>" +loan_data["principal_amount"] +"</td>";
    table_html += "</tr>";
    # ----------------------------------------
    table_html += "<tr>";
    table_html += "<td>Monthly Amortization</td>";
    table_html += "<td>" +loan_data["monthly_amortization"] +"</td>";
    table_html += "</tr>";
    # ----------------------------------------
    table_html += "<tr>";
    table_html += "<td>Total Interest</td>";
    table_html += "<td>" +loan_data["total_interest"] +"</td>";
    table_html += "</tr>";
    # ----------------------------------------
    table_html += "<tr>";
    table_html += "<td>Loan Term</td>";
    table_html += "<td>" +loan_data["loan_terms"] +" month(s)</td>";
    table_html += "</tr>";
    # ----------------------------------------
    table_html += "<tr>";
    table_html += "<td>Total Sum of Payments upon Loan Maturity</td>";
    table_html += "<td>" +loan_data["total_sum_upon_maturity"] +"</td>";
    table_html += "</tr>";
    # ----------------------------------------
    table_html += "<tr>";
    table_html += "<td>First Loan Payment Date</td>";
    table_html += "<td>" +loan_data["first_loan_payment_date"] +"</td>";
    table_html += "</tr>";
    # ----------------------------------------
    table_html += "<tr>";
    table_html += "<td>Loan Maturity Date</td>";
    table_html += "<td>" +loan_data["loan_maturity_date"] +"</td>";
    table_html += "</tr>";
    table_html += "</table>"

    subject = "YOUR LOAN DETAILS FROM GOLDEN FINANCING"
    message_html = "<p>Dear " + customer.fullname + ", </p>"
    message_html += "<p>Loan Details</p>"
    message_html += table_html
    message_html += "<p>Thank you</p>"

    print(message_html)

    # Send Email
    mail = EmailMultiAlternatives(subject, "", settings.EMAIL_HOST_USER, [customer.email])
    mail.attach_alternative(message_html, "text/html")
    mail.send()


def loan_summary(loan, is_email=False):
    if loan.loan_type=="A":
        monthly_amortization = get_monthly_amortization(loan.loan_terms, loan.loan_amount)
    else:
        monthly_amortization = loan.loan_amortization
    total_interest = get_total_interest(loan.loan_amount, monthly_amortization, loan.loan_terms)
    total_sum_upon_maturity = get_total_sum_upon_maturity(monthly_amortization, loan.loan_terms)

    data = {
        "loan_id": loan.id,
        "principal_amount": currency_format(loan.loan_amount),
        "monthly_amortization": currency_format(monthly_amortization),
        "total_interest": currency_format(total_interest),
        "loan_terms": str(int(loan.loan_terms)),
        "total_sum_upon_maturity": currency_format(total_sum_upon_maturity),
        "first_loan_payment_date": get_first_loan_payment_date(),
        "loan_maturity_date": get_loan_maturity_date(loan.created_at, loan.loan_terms)
    }

    if is_email:
        send_email(data)
    return data