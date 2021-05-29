from django.db import models

class LoanDetails(models.Model):
    loan_type = models.CharField(max_length=255, null=True, blank=True)
    loan_amount = models.FloatField(default=0)
    loan_amortization = models.FloatField(default=0)
    loan_terms = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.loan_type + " - " + str(self.loan_amount)

    class Meta:
        verbose_name = "Loan Detail"
        verbose_name_plural = "Loan Details"

class Customer(models.Model):
    loan = models.ForeignKey(
        LoanDetails,
        on_delete=models.SET_NULL,
        related_name="loan_customer",
        null=True, blank=True
    )
    fullname = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    mobile_number = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    province = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return self.fullname

    class Meta:
        verbose_name = "Customer"
        verbose_name_plural = "Customers"