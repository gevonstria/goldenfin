from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.generic import View
from django.http import JsonResponse
from backend.models import LoanDetails, Customer
import json

class LogIn(View):

    def post(self, request):
        post_data = json.loads(request.body)
        user = authenticate(username=post_data["username"], password=post_data["password"])
        if user is not None:
            message = "valid"
        else:
            message = "invalid"
            # No backend authenticated the credentials
        return JsonResponse({"message": message})

class Loan(View):

    def get(self, request):
        table_list = []
        customers = Customer.objects.all()
        for cust in customers:
            data = {
                "id": cust.id,
                "loan_type": cust.loan.loan_type,
                "loan_amount": cust.loan.loan_amount,
                "fullname": cust.fullname,
                "city": cust.city
            }
            table_list.append(data)

        return JsonResponse({"data": table_list})


    def post(self, request):
        post_data = json.loads(request.body)
        print(post_data)
        # try:
        # Loan Details
        new_loan = LoanDetails()
        new_loan.loan_type = post_data["loan_type"]
        new_loan.loan_amount = post_data["loan_amount"]
        new_loan.loan_amortization = post_data["loan_amortization"]
        new_loan.loan_terms = post_data["loan_terms"]
        new_loan.save()

        # Customer
        new_customer = Customer()
        new_customer.loan = new_loan
        new_customer.fullname =post_data["fullname"]
        new_customer.email = post_data["email"]
        new_customer.mobile_number = post_data["mobile_number"]
        new_customer.city = post_data["city"]
        new_customer.province = post_data["province"]
        new_customer.save()

        # except Exception as e:
        #     message = e

        message = "success"
        return JsonResponse({"message": message})

